{
  description = "dlpeterson.com — Zola site devshell";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs }:
    let
      supportedSystems = [ "x86_64-linux" "aarch64-darwin" ]; # linux now, possible future mac
      eachSupportedSystem = nixpkgs.lib.genAttrs supportedSystems;
    in {
      devShells = eachSupportedSystem (system:
        let pkgs = import nixpkgs { inherit system; };
        in {
          default = pkgs.mkShell {
            packages = [ pkgs.zola ];
            shellHook = ''echo "zola $(zola --version)"'';
          };
        });
    };
}
