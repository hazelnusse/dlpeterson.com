{
  description = "dlpeterson.com — Zola site devshell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";
  inputs.treefmt-nix.url = "github:numtide/treefmt-nix";

  outputs = { self, nixpkgs, treefmt-nix }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-darwin" ]; # linux now, possible future mac
      eachSupportedSystem = nixpkgs.lib.genAttrs supportedSystems;
      treefmtEval = eachSupportedSystem (system:
        let
          pkgs = import nixpkgs { inherit system; };
          # prettier-plugin-jinja-template requires `prettier` to be resolvable
          # from its own node_modules, but nixpkgs packages them as separate
          # store paths. NODE_PATH is a supplementary module search path Node
          # always checks, independent of symlink resolution, so wrap prettier
          # to set it rather than trying to merge the two store paths.
          prettierWithJinja = pkgs.writeShellApplication {
            name = "prettier";
            text = ''
              export NODE_PATH="${pkgs.prettier}/lib/node_modules"
              exec "${pkgs.prettier}/bin/prettier" "$@"
            '';
          };
        in
        treefmt-nix.lib.evalModule pkgs {
          projectRootFile = "flake.nix";
          programs.prettier = {
            enable = true; # .md, .css, .html (as Jinja/Tera templates)
            package = prettierWithJinja;
            settings = {
              plugins = [
                "${pkgs.prettier-plugin-jinja-template}/lib/node_modules/prettier-plugin-jinja-template/lib/index.js"
              ];
              overrides = [
                {
                  files = [ "*.html" ];
                  options.parser = "jinja-template";
                }
              ];
            };
          };
          programs.taplo.enable = true; # .toml
        });
    in {
      devShells = eachSupportedSystem (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.mkShell {
            packages = [ pkgs.zola ];
            shellHook = ''echo "zola $(zola --version)"'';
          };
        });

      formatter = eachSupportedSystem (system: treefmtEval.${system}.config.build.wrapper);

      checks = eachSupportedSystem (system: {
        formatting = treefmtEval.${system}.config.build.check self;
      });
    };
}
