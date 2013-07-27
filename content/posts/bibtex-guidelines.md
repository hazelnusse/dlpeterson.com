date: 2013-07-27 07:25
title: Guidelines for BibTeX & Mendeley
category: Notes
tags: bibtex, mendeley, latex

I recently began the monumental task of reorganizing my collection of pdfs.
During my time in grad school, I amassed a large collection. They started out
pretty organized, but several pdf/bibtex management systems system re-installs
(JabRef, Mendeley) later, I had all sorts of errors: duplicated pdfs, incorrect
citations, and missing pdfs. What a pain!

In the process of cleaning things up, I took the time to carefully understand
how Mendeley does things. Here are the settings I am using to remind myself
what I need to backup:

* A database directory: `~/.local/share/data/Mendeley Ltd./Mendeley Desktop`
* A directory of organized pdfs, I use: `~/Documents/MendeleyManagedPapers`
* A directory to watch for new pdfs, I use: `~/Downloads/MendeleyWatched`
* A master BibTeX file, I use: `~/Documents/MendeleyManagedPapers/library.bib`

Adding files to Mendeley can be accomplished any of the following ways:

* For files already on your computer (but not in the watched directory),
  launch Mendeley, choose `Add Files` from toolbar.
* Launch Mendeley, save pdfs to `~/Downloads/MendeleyWatched`
* While in browser, visit a publishers website, navigate to the paper, and
  choose the `Save to Mendeley` bookmark in the browser bar. If that bookmark
  isn't there, directions to add it are [here](http://www.mendeley.com/import/).

Once you import the file, make sure you check the citation info, it is
generally not well formatted, and possibly incorrect. Here are the guidelines
to follow for the citation (essentially a BibTeX entry):

* Space between authors' initials, dot after each initial. The BibTeX style
  will decide the spacing in print.
* All significant words in the title are
  capitalized. The style will decide if to change to lowercase or not.
* Protect letters in the title that should stay uppercase (but nothing else)
  by { }.
* -- for the proper long dash

These guidelines and a few more came from
[here](http://ccm.ucdenver.edu/wiki/How_to_write_BibTeX_files).

