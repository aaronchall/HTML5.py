=====
HTML5
=====

HTML5 is a Python lib to create standards compliant html. 

Given Python code with 
well-written docstrings and argument specifications (really
nice autocompletion and assistance by online helps)::

          Article([H1('Top Level Heading in an Article'), 
                   P(['This is a paragraph under the article'], Class='Foo'),
                   Comment(['this is a <comment>, all kinds of '
                            '<weirdness> can be hidden from parsing']),
                   H2('2nd level heading in the Article'),
                   P(['Another paragraph, with a {link} to back it up.'.format(
                        link=A('http://foo/bar', 'linky'))]),
                  ]),

We output really well-defined HTML5::

  <article>
    <h1>
      Top Level Heading in an Article
    </h1>
    <p Class="Foo">
      This is a paragraph under the article
    </p>
    <!--
      this is a <comment>, all kinds of <weirdness> can be hidden from parsing
    //-->
    <h2>
      2nd level heading in the Article
    </h2>
    <p>
      Another paragraph, with a <a href="http://foo/bar">
        linky
      </a> to back it up.
    </p>
  </article>


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

Run tests with either of the following::

    $ python -m nose
    $ nosetests

=====
TODOs
=====

- write unittests
- write acceptance tests (end to end)
- write docs
- make documented helper functions for input objects in forms module
- improve documentation on preexisting objects
- ``.gitignore`` ignores ``*index.html`` - is that ok?
- POSTPONED: make some ``__all__`` lists for the modules
