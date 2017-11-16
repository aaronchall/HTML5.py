"""emulate the html from html5boilerplate"""
from __future__ import print_function, division, absolute_import 
from html5 import Document, Head, Meta, Description, Viewport, Link
from html5 import Script, Body, Comment, Paragraph
from html5 import Description, Viewport# metas



def main():
    """print the boilerplate"""
    print(
      Document(
        Head(
          [Meta(http-equiv='x-ua-compatible', content='ie=edge'), # get charset for free
           Description('Boilerplate has this empty, but '
                       'this description should be detailed '
                       'it is what will show up in Google'),
           Viewport('width=device-width, initial-scale=1'),
           Link(rel='apple-touch-icon', href='apple-touch-icon.png'),
           # maybe we need comments for this sort of thing:
           Comment('Place favicon.ico in the root directory'),
           Link(rel='stylesheet', href='css/normalize.css'),
           Link(rel='stylesheet', href='css/main.css'),

           ],
           
          title=Title('')), 
        Body([
          #Comment("""[if lt IE 8]>
          #        <p class="browserupgrade">You are using an <strong>outdated</strong> browser. Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience.</p>
          #        <![endif]""")
          Conditional(
            'if lt IE 8'
            [Paragraph(["""<p class="browserupgrade">You are using an <strong>outdated</strong> browser. 
                         Please <a href="http://browsehappy.com/">upgrade your browser</a> to improve your experience."""],
                       Class='browserupgrade', )],
          ),
          # are comments necessary? We have Python comments. Why have no-op html?
          Comment('Add your site or application content here'),
          Script(src='https://ajax.googleapis.com/ajax/libs/jquery/{{JQUERY_VERSION}}/jquery.min.js'),
          Script(["""window.jQuery || document.write('<script src="js/vendor/jquery-{{JQUERY_VERSION}}.min.js"><\/script>')'"""]),
          Script(src="js/plugins.js"),
          Script(src="js/main.js"),
        
        ]),
        Class='no-js'
        )
    )

if __name__ == '__main__':
    main()
