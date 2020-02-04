# CodeCheck by Esther He | February 3, 2020

CodeCheck.py, an automated code checker that simplifies code documentation.

CodeCheck.py takes in a valid input file and outputs the following:
  Total # of lines:
  Total # of comment lines:
  Total # of single line comments:
  Total # of comment lines within block comments:
  Total # of block line comments:
  Total # of TODO’s:

Note: a valid input file is defined as a file with a filename that does not start with '.', and contains an extension

Assumptions:
1. Docstrings are ignored.
2. Block comments are consecutive lines that start with a '#'.
3. A single line comment is a line that starts with a '#', but does not belong to a block comment.
4. TODO lines are lines that start with '# TODO'. If a TODO line does not belong to a block comment, it is then counted as a single line comment.
5. Inline comments count as single line commnets, but are not counted towards bloack comments.
