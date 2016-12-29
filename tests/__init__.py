from __future__ import print_function, division, absolute_import
import unittest
import os
import sys
import inspect
import re
import traceback

#currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
#parentdir = os.path.dirname(currentdir)
#sys.path.append(parentdir)

from html5 import *


class HTML5Test(unittest.TestCase):

    def test_head(self):
        """Heads guarantee a (if default) title"""
        regex = re.compile(r'\s*<head>\s*<title>\s*Foo\s*</title>.*</head>.*', re.DOTALL)
        self.assertRegexpMatches(Head(title='Foo'), regex)

    def test_body(self):
        regex = re.compile(r'<body>\s*</body>')
        self.assertRegexpMatches(Body(), regex)
       
    def test_hyperlink(self):
        hl = HyperLink('bar/link', 'bar text')
        self.assertRegexpMatches(hl, r'\s*<a href="bar/link">\s*bar text\s*</a>')

    def test_h1(self):
        h1 = H1('something')
        self.assertRegexpMatches(h1, r'\s*<h1>\s*something\s*</h1>')
    
    def test_all_call(self):
        """"""
        import html5
        names = set(n for n in dir(html5) if n[0].isupper())
        all_objects = (getattr(html5, n) for n in dir(html5))
        objects = set(obj for obj in all_objects if isinstance(obj, html5.Elem))
        nargs = set(), set(), set()
        args = 'foo', 'bar'
        for i in range(3):
            print(('{0} args' + '*'*60).format(i))
            for name in sorted(names, key=):
                try:
                    obj = getattr(html5, name)(*(args[:i]))
                except Exception as error:
                    pass
                else:
                    print(repr(obj))
                    print(obj)
                    nargs[i].add(name)
        errored_all = names - nargs[0] - nargs[1] - nargs[2]
        if errored_all:
            self.fail(errored_all, 
                      'at this time, do not expect more than 2 required args per obect')
        # expect to assert some names will/will not be in some of the successfully
        # called sets
                    
    def test_acceptance(self):
        nav = Nav([
          H1('Nav Section'),
          UnorderedList([ListItem([HyperLink('foo/link', 'foo text')]), 
                         ListItem([HyperLink('bar/link', 'bar text')])])])
        head = Head(title='Example',
                    # elems almost always comes first but I like title as first when possible.
                    elems=[Keywords(['python', 'html', 'C++', 'C', 'assembly']),
                           Description('demo page'),
                           Author('Aaron Hall'),
                           Robots(),
                           Link(rel='stylesheet', 
                                href='http://yui.yahooapis.com/pure/0.6.0/pure-min.css'),
        ])
        form = Form([
            Input('foo', 'FooStart', readonly=True), Br(),
            Input('email', '', autocomplete=True), Br(),
            Input('baz', 'Baz Start', disabled=True), Br(),
            Input('boink', 'Boink Start', maxlength=10), Br(),
        ])
        section = Section([H1('Heading 1 a section... but of what?'), 
                       P(['Below is a form, like a survey maybe']),
                       form,
                       H1('Here is a canvas:'),
                       Canvas(id='a_canvas_object', width=400, height=100, 
                              style='background-color:#333'),
        ])
        article = Article([H1('Top Level Heading in an Article'), 
                       P(['This is a paragraph under the article'], Class='Foo'),
                       Comment(['this is a <comment>, all kinds of '
                                '<weirdness> can be hidden from parsing']),
                       H2('2nd level heading in the Article'),
                       P(['Another paragraph, with a {link} to back it up.'.format(
                            link=A('http://foo/bar', 'linky'))]),
        ])
        aside = Aside(['This "aside" could be a floaty sidebar, or a callout,'
                     ' or a quote from the article... not sure if it goes '
                     'inside the article or not...', Br(),
                     Img('https://projecteuler.net/profile/aaronchall.png'),Br(),
                     Img('http://stackexchange.com/users/flair/258754.png?theme=dark'),Br(),
                     Img('http://stackoverflow.com/users/flair/541136.png?theme=dark')
        ])
        header = Header([
                H1('Header Section, Title of Doc.'), P(['SVG:']),
                SVG([
                  Circle(cx=50, cy=50, r=40, stroke="green", fill="yellow")], #stroke-width=4, 
                width=100, height=100),
                P(['End of Header'])  
        ])
        footer = Footer([
            H4('A lovely little Footer'),
            'Maybe this footer could float on the side on a wide screen', nav,
            Address(['Contact Info', Br(), EmailLink('aaronchall@yahoo.com', 'Email Me!'),
            Br(), HyperLink('/', 'Home')]),
        ])

        htmlobjs = Document(
          head=head,
          body=Body([
              header,
              nav,
              section,
              article,
              aside,          
              footer,
          ]),
        )
