=====
HTML5
=====

HTML5 is a Python lib to create compliant html.  (see docstrings)

============
Installation
============

Ideally, to install we will have set up pip, but we haven't yet::

    $ pip install html5

============
Contributing
============

You can get a local copy to make contributions with this::

    $ git clone http://www.github.com/aaronchall/html5.py

Note that we don't yet have an ``__all__``, we're going to stick to the
convention that exported names don't start with an ``_``. So
if we need to import a stdlib module, alias it to be prefixed with an ``_``.
Also name helper functions not intended for export by prefixing an ``_``.
Also do not ever name anything "helper".

Test out the main with::

    $ python html5

Test the setup.py and README.rst (this file) with::

    $  python setup.py check --restructuredtext

=====
TODOs
=====


- write unittests
- write acceptance tests (end to end)
- write docs
- make documented helper functions for input objects in forms module
- improve documentation on 
- .gitignore ignores *index.html - is that ok?
- POSTPONED: make some ``__all__`` lists for the modules
