

Building an interpreter
=======================

This repo holds some examples of interpreters I have been building for
educational purposes. The ``calc`` subdir contains sources for a simple
arithmetic expression interpreter (basically a calculater, hence the name).
There is a version that uses PLY as a parser generator (``calc/shelf.py``)
and a version where the lexer and parser have been written by hand (``calc/homebrew.py``),
whereas the latter one was mostly inspired by this [blog post series](http://ruslanspivak.com/lsbasi-part6/)
