from __future__ import division, absolute_import, print_function
from html5 import *


def main():
    nav = Nav([
      H1('Nav Section'),
      UnorderedList([ListItem([HyperLink('foo/link', 'foo text')]), 
                     ListItem([HyperLink('bar/link', 'bar text')])])])
    htmlobjs = Document(
      head=Head(title='Example',
                # elems almost always comes first but I like title as first when possible.
                elems=[Keywords(['python', 'html', 'C++', 'C', 'assembly']),
                       Description('demo page'),
                       Author('Aaron Hall'),
                       Robots(),
                       Link(rel='stylesheet', 
                            href='http://yui.yahooapis.com/pure/0.6.0/pure-min.css'),
                      ]),
      body=Body([
          Header([
            H1('Header Section, Title of Doc.'), P(['SVG:']),
            SVG([
              Circle(cx=50, cy=50, r=40, stroke="green", fill="yellow")], #stroke-width=4, 
            width=100, height=100),
            P(['End of Header'])  
          ]),
          nav,
          Section([H1('Heading 1 a section... but of what?'), 
                   P(['Below is a form, like a survey maybe']),
                   Form([
                       Input('foo', 'FooStart', readonly=True), Br(),
                       Input('email', '', autocomplete=True), Br(),
                       Input('baz', 'Baz Start', disabled=True), Br(),
                       Input('boink', 'Boink Start', maxlength=10), Br(),
                       ]),
                   H1('Here is a canvas:'),
                   Canvas(id='a_canvas_object', width=400, height=100, 
                          style='background-color:#333'),
                 ]),
          Article([H1('Top Level Heading in an Article'), 
                   P(['This is a paragraph under the article'], Class='Foo'),
                   Comment(['this is a <comment>, all kinds of '
                            '<weirdness> can be hidden from parsing']),
                   H2('2nd level heading in the Article'),
                   P(['Another paragraph, with a {link} to back it up.'.format(
                        link=A('http://foo/bar', 'linky'))]),
                  ]),
          Aside(['This "aside" could be a floaty sidebar, or a callout,'
                 ' or a quote from the article... not sure if it goes '
                 'inside the article or not...', Br(),
                 Img('https://projecteuler.net/profile/aaronchall.png'),Br(),
                 Img('http://stackexchange.com/users/flair/258754.png?theme=dark'),Br(),
                 Img('http://stackoverflow.com/users/flair/541136.png?theme=dark')
                 ]),          
          Footer([
              H4('A lovely little Footer'),
              'Maybe this footer could float on the side on a wide screen', nav,
              Address(['Contact Info', Br(), EmailLink('aaronchall@yahoo.com', 'Email Me!'), 
                       Br(), HyperLink('/', 'Home')]),
          ]),
       ]),
    )
    print('*****'*20)
    print(htmlobjs)
    writeout(htmlobjs, 'index.html')
    print(repr(htmlobjs))
    # assert test below fails... :(
    #assert htmlobjs == eval(repr(htmlobjs))

if __name__ == '__main__':
    main()
