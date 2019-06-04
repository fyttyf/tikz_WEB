#!/bin/sh
cd ./data/compile/$1
latex $1.tex
bibtex $1
latex $1.tex
latex $1.tex
dvipdf $1.dvi ../../pdf/$1.pdf
