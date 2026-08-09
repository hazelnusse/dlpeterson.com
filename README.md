# dlpeterson.com

Personal site and blog, built with [Zola](https://www.getzola.org/). The dev
environment is a [Nix](https://nixos.org/) flake, so the only prerequisite on
any machine is Nix with flakes enabled.

## Getting started

```
nix develop
```

drops you into a shell with the pinned `zola` binary on `PATH`. If you use
[direnv](https://direnv.net/), `direnv allow` once and the shell loads
automatically on `cd`.

## Local dev server

```
zola serve
```

Serves the site at http://127.0.0.1:1111 with live-reload on file changes.

## Adding a blog post

Create a new directory under `content/blog/` with an `index.md`:

```
mkdir content/blog/my-new-post
```

```markdown
+++
title = "My New Post"
date = 2026-08-08T12:00:00-07:00

[taxonomies]
tags = ["some-tag"]
+++

Post body in Markdown goes here.
```

The `[taxonomies]` block is optional — omit it for an untagged post. The post
will appear at `/blog/my-new-post/`. Any files placed alongside `index.md` in
the same directory (images, PDFs, etc.) are copied through as-is and can be
linked with a relative path.

## Editing the resume

The resume lives at `content/resume.md` and renders through
`templates/resume.html`, a standalone template (no site nav/header) with a
`static/css/print.css` stylesheet scoped to `@media print` so it prints
cleanly to one page from the browser's print dialog. If you add content,
re-check the page count — e.g. render it headlessly and check with a PDF
tool:

```
zola serve &
nix shell nixpkgs#chromium --command chromium --headless --disable-gpu \
  --no-sandbox --print-to-pdf=/tmp/resume.pdf http://127.0.0.1:1111/resume/
nix shell nixpkgs#poppler-utils --command pdfinfo /tmp/resume.pdf | grep Pages
```

## Building for production

```
zola build
```

Outputs the static site to `public/` (gitignored).

## Netlify hosting

The site deploys on [Netlify](https://www.netlify.com/), building straight
from this repo — push to `master` and it deploys automatically. Config lives
in `netlify.toml`:

- **Build command**: `zola build`, publishing the `public/` directory.
- **Zola version**: pinned via the `ZOLA_VERSION` build environment
  variable, using Netlify's `binrc` mechanism to fetch that exact tagged
  Zola binary — no Nix involved in the Netlify build image itself. When
  bumping the Zola version, update `ZOLA_VERSION` in `netlify.toml` _and_
  run `nix flake update` locally so the devshell and Netlify stay in sync.
- **Deploy previews / branch deploys**: build with `--base-url
$DEPLOY_PRIME_URL` so links resolve against the preview URL instead of
  the production domain.
- **Custom domain**: `dlpeterson.com` (and `www.dlpeterson.com`, which
  redirects to the apex) is configured directly in the Netlify dashboard
  under Domain settings — there's no `CNAME` file in this repo (that's a
  GitHub Pages convention and isn't used here).
- **HSTS**: applied to all routes via the `[[headers]]` block in
  `netlify.toml`.

To check or change domain/DNS settings, use the Netlify dashboard for this
site (Site settings → Domain management) rather than anything in this repo.
