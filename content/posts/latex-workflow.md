date: 2013-08-09 00:25
title: LaTeX workflow
category: Notes
tags: latex, bibtex, biber, xelatex

In the last several years, the common workflow for using LaTeX has changed
since I first learned it. In particular, bibtex has been to a large degree
superseded by [biblatex-biber](http://biblatex-biber.sourceforge.net/).
Additionally, while I used to use
[pdftex](http://www.tug.org/applications/pdftex/) to build pdfs, it doesn't
support unicode. After reading [Joel Spolsky's article about
unicode](http://www.joelonsoftware.com/articles/Unicode.html), I decided this
is a hard requirement, so pdftex was out.  The
[XeTeX](http://xetex.sourceforge.net/) and [LuaTeX](http://www.luatex.org/)
projects have addressed this issue, it seems like XeTeX is more mainstream.
Finally, for the actually build process, I used things like
[Vim-LaTeX](http://vim-latex.sourceforge.net/) or
[AucTeX](http://www.gnu.org/software/auctex/) (or sometimes a manually written
`Makefile`). The [latexmk](http://www.ctan.org/pkg/latexmk/) package (not to be
confused with the [LaTeX-Mk](http://latex-mk.sourceforge.net/) package, which
hasn't seen an update since 2010-12-28 and is *not* part of the MikTeX
distribution) now does an excellent job of managing the building of your pdf.
This post outlines my new work flow that takes advantage of the latest tools in
the TeX/LaTeX world.

First, install [TeX Live](http://www.tug.org/texlive/) (use your package
manager if you can so you automatically will get updates). The first thing to
set up is latexmk. latexmk has a few options that are worth configuring (`man
latexmk` will give you all the gory details). I set the following in my
`~/.latexmkrc`:

```bash
# Choose xelatex as the default builder of pdfs, don't stop for errors, use synctex
$pdflatex = 'xelatex -interaction=nonstopmode -synctex=1 --shell-escape %O %S';
# .bbl files assumed to be regeneratable, safe as long as the .bib file is available
$bibtex_use = 2;
# User biber instead of bibtex
$biber = 'biber --debug %O %S';
# Default pdf viewer
$pdf_previewer = 'evince %O %S';
# Extra file extensions to clean when latexmk -c or latexmk -C is used
$clean_ext = '%R.run.xml %R.synctex.gz';
```

Open up your favorite editor and create `mwe.tex` with the following contents

```latex
\documentclass{article}

\usepackage[
  backend=biber,
]{biblatex}
\addbibresource{references.bib}

\usepackage[
  pdfencoding=auto,
]{hyperref}

\begin{document}
Numbering should start at zero~\cite{EWD831}.
\end{document}
```

and `references.bib` with

```latex
@unpublished{EWD831,
  author = {Dijkstra, Edsger W.},
  pages = {3},
  title = {{Why numbering should start at zero}},
  url = {http://www.cs.utexas.edu/users/EWD/ewd08xx/EWD831.PDF},
  year = {1982}
}
```

Now to have latexmk build `mwe.tex` into the pdf enter this into your terminal

```bash
$ latexmk -pvc -pdf ./mwe.tex
```

This should immediately build your pdf and open it up using `evince`. In
another terminal, start editing the .tex file or the .bib file. As soon as you
save, `mwe.pdf` should automatically be rebuilt and the updated result shown in
evince. If you have your editor open next to evince, all you have to do is save
the file and the pdf will be updated. This can sometimes be problematic if
there are build errors, but the `-interaction=nonstopmode` will prevent the
build from hanging so once you fix the problem it should automatically get
fixed. latexmk automatically determines dependencies, so if you have files
included/input into your main .tex file, it will update the build appropriately
as soon as it detects a change to the file (not just a time stamp change, but
an actual content change).

I haven't yet gotten synctex to work with vim, but that option is enabled above
so it should just be a matter of figuring out how to configure vim correctly.
I'll leave that for another day. Also, there is another TeX build automation
tool called [arara](https://github.com/cereda/arara) that looks pretty
promising. It looked like a bit more work and it didn't come bundled with
TeXLive, so I stuck with latexmk, but I'll keep an eye on arara down the road.



