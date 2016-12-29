""" document/__init__.py
This package is for Python coders who have at least a passing familiarity 
with html, but do not wish to write it.

The objects can also be use programmatically to create static pages or 
(potentially) templates. 

This package expects to make it easy to write compliant, well-formed, SEO,
and best-practice html5. 

SEO notes from moz.com and google

New HTML5 elements checkoff list, delete as added:
<bdi> Defines a part of text that might be formatted in a different direction from other text
<details> Defines additional details that the user can view or hide
<dialog> Defines a dialog box or window
<figcaption> Defines a caption for a <figure> element
<figure> Defines self-contained content, like illustrations, diagrams, photos, code listings, etc.
<main> Defines the main content of a document
<mark> Defines marked or highlighted text
<menuitem>  Defines a command/menu item that the user can invoke from a popup menu
<meter> Defines a scalar measurement within a known range (a gauge)
<progress> Defines the progress of a task
<rp> Defines what to show in browsers that do not support ruby annotations
<rt> Defines an explanation/pronunciation of characters (for East Asian typography)
<ruby> Defines a ruby annotation (for East Asian typography)
<section> Defines a section in the document
<summary> Defines a visible heading for a <details> element
<time> Defines a date/time
<wbr> Defines a possible line-break

Form elements, delete as added:
<datalist> Defines pre-defined options for input controls
<keygen> Defines a key-pair generator field (for forms)
<output> Defines the result of a calculation
"""
from __future__ import division, absolute_import, print_function
from pipes import quote as _quote
import sys as _sys
print('executing document/__init__.py, name, sys.argv:')
print(__name__)
print(' '.join(_quote(s) for s in _sys.argv))

#__all__ = ['A', 'Abbr', 'Address', 'Anchor', 'Area', 'Article',
#           'Aside', 'Audio', 'Author', 'Base', 'Blockquote', 'Body',
#           'Br', 'Canvas', 'Circle', 'Code', 'Comment', 'Datalist',
#           'Description', 'Details', 'Document', 'Elem', 'ElemContainer',
#           'EmailLink', 'Embed', 'Footer', 'Form', 'H1', 'H2', 'H3', 'H4',
#           'H5', 'H6', 'Head', 'Header', 'HyperLink', 'Image', 'Img', 'Input',
#           'KBD', 'Keywords', 'LI', 'LineBreak', 'Link', 'ListItem', 'Map',
#           'Meta', 'Nav', 'OL', 'Option', 'OrderedList', 'P', 'Paragraph',
#           'Q', 'QuoteInline', 'Robots', 'SVG', 'Samp', 'Script', 'Section',
#           'Source', 'TextOnly', 'Title', 'Track', 'UL', 'UnorderedList',
#           'Var', 'Video', 'writeout']

def _indent(html, space='  '):
    '''use this on elem.__str__ return value not at root'''
    # list comp because join has to go over twice anyways
    return '\n'.join([space + s if s else s for s in html.splitlines()])

def _init_names(self, names):
    for name, value in names.items():
        if value is not None and name not in ('self', 'cls'):
            setattr(self, name, value)

class Document(object):
    """
    Documents require a Head and a Body XXX elaborate
    Can give title if head is not given.
    >>> d = Document(Head(title='Example'), Body())
    >>> d
    Document(lang='en', body=Body(elems=[]), head=Head(
      elems=[Title(elems=['Example']), Meta(charset='UTF-8')]), doctype='html')
    >>> print(d)
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <title>
        Example
      </title>
        <meta charset="UTF-8">
    </head>
    <body>

    </body>
    </html>
    """
    template = '<!DOCTYPE {doctype}>\n<html lang="{lang}">\n{head}\n{body}\n</html>'
    def __init__(self, head='', body='',
                 doctype='html', lang='en', title=''):
        if not head:
            head = Head(title=title)
        elif title:
            raise ValueError('head given, declare title in head')
        _init_names(self, locals())
    def __repr__(self):
        kwargs = ', '.join(k+'='+repr(arg) for k, arg in self.__dict__.items() if arg)
        return '{0}({1})'.format(type(self).__name__, kwargs)
    def __str__(self):
        return self.template.format(**self.__dict__)

class Elem(str):
    """
    base class for elements, no closing tag, ElemContainer 
    subclasses this and closes tags
    "There are also tags that are forbidden to be closed: img, input, br, hr, meta,"
    """
    template = '<{name}{kwargs}>'
    def __new__(cls, elems=[], **kwargs):
        if isinstance(elems, str):
            elems = [elems] # elems will be stored in a list.
        if elems:
            kwargs['elems'] = elems
        string = cls._to_str(cls._html_args(kwargs), elems) # formatted
        self = super(Elem, cls).__new__(cls, string)
        _init_names(self, kwargs)
        return self

    def __repr__(self):
        kwargs = ', '.join(k+'='+repr(arg) for k, arg in self.__dict__.items())
        return '{0}({1})'.format(type(self).__name__, kwargs)
    def __str__(self):
        return _indent(self._to_str(self._html_args(self.__dict__),
                                    self.__dict__.get('elems', [])))
    @classmethod
    def _to_str(cls, htmlargs, elems=None):
        ### Only expect elems for subclasses, don't use it here.
        return cls.template.format(name=cls._name(), kwargs=htmlargs)
    def __eq__(self, other):
        return type(self) is type(other) and self.__dict__ == other.__dict__
    @staticmethod
    def _html_args(d):
        return ''.join([
            ' {0}="{1}"'.format(k, v) 
          if not isinstance(v, bool) 
            else ' ' + k                   #method="post" action="" same as deleting action
              for k, v in d.items()        # if v is '' and "" is a valid
                if v and k not in ('elems',)])  # html tag kwarg, this is wrong. 
    @classmethod
    def _name(cls):
        return cls.__name__.lower()
    
class ElemContainer(Elem):
    """unless forbidden to close, most elements should use this base class"""
    template = '<{name}{kwargs}>\n{elems}\n</{name}>'

    @classmethod
    def _to_str(cls, htmlargs, elems=[]):
        elemstr = _indent('\n'.join(str(e) for e in elems))
        return cls.template.format(
          name=cls._name(), kwargs=htmlargs, elems=elemstr)
    

class Head(ElemContainer):
    '''in html5, head can be omitted.
    can have:
    <title> (this element is required in an HTML document)
    <style>
    <base>
    <link>
    <meta> (must go in a head)
    <script>
    <noscript>
    '''
    def __new__(cls, elems=[], charset='UTF-8', style='', title='Default Title'):
        elems = [Title(title), Meta(charset=charset)]
        if style and isinstance(style, Style):
            elems.append(style)            
        elif style:
            elems.append(Style(style=style))
        elems.extend(elems)
        return super(Head, cls).__new__(cls, elems)


class TextOnly(ElemContainer):
    """these things might only have a single item in them, logic pushed into base class"""


class Title(TextOnly):
    """
    this should be in all html5 docs, can be in head or exclude head above body
    Important for SEO, make this a Full Title.
    """

class H1(TextOnly): """Level 1 heading"""
class H2(TextOnly): """Level 2 heading"""
class H3(TextOnly): """Level 3 heading"""
class H4(TextOnly): """Level 4 heading"""
class H5(TextOnly): """Level 5 heading"""
class H6(TextOnly): """Level 6 heading"""

class KBD(TextOnly): """keyboard input"""
class Var(TextOnly): """variable name"""
class Code(TextOnly): """computer code"""
class Samp(TextOnly): """computer output"""

class Comment(ElemContainer): 
    """Comment out html or javascript """
    template = '<!--\n{elems}\n//-->'

class Script(ElemContainer):
    """bad idea to include JS? take out?"""
    #def __init__(self, elems=[], type='text/javascript', async=False,
    #             charset=None, defer=False, src=None):
    #    _init_names(self, locals())

class Meta(Elem):
    """Goes in head.
    Robots, Author, Keywords, Description (maybe more) return this object.
    """

def Robots(content='index, follow'):
    """
    Superior to robots.txt according to moz
    >>> Robots()
    <meta name="robots" content="index, follow">
    >>> Robots(content='index, nofollow')
    <meta name="robots" content="index, nofollow">
    """
    if isinstance(content, (tuple, list)):
        content = ','.join(content)
    return Meta(name='robots', content=content)

def Author(author_name):
    """return meta element with author info for head"""
    return Meta(name='author', content=author_name)

def Keywords(words):
    """return meta element with keywords info for head"""
    if not isinstance(words, str):
        words = ', '.join(words)
    return Meta(name='keywords', content=words)

def Description(desc):
    """return meta element with description for head"""
    return Meta(name='description', content=desc)

def Viewport(content):
    """e.g. Viewport('width=device-width, initial-scale=1')"""
    return Meta(name='viewport', content=content)

class Base(Elem):
    """One base per doc, in head
    Make first head element so all other things can use it.
    This is the base of all urls on page
    Target can be any of 

    '_blank', '_parent', '_self', '_top', 
    or a framename.

    >>> print(Base('http://www.example.com/images/', '_blank'
    <base href="http://www.example.com/images/" target="_blank">
    """
    def __new__(cls, href, target):
        return super(Base, cls).__new__(cls, href=href, target=target)


class Link(Elem):
    """
    link outside documents, e.g. (mostly) CSS -- goes in head.
    href: url
    hreflang: language code
    media: media query
    sizes: '{}x{}'.format(height, width) (for rel="icon")
    crossorigin: anonymous or use-credentials
    type: IANA media - see www.iana.org/assignments/media-types/media-types.xhtml
    rel='' links to:
      "alternate" version of document (i.e. print page, translated or mirror).
      "author" of the document
      "help"
      "icon" imports to represent the document.
      "license" copyright information for the document
      "next" document in implied series
      "prefetch" cache target resource
      "prev" document in implied series
      "search" tool for the document
      "stylesheet" url to import
      also: archives bookmark external first last nofollow noreferrer pingback
            sidebar tag up
    >>> Link(rel='stylesheet', type='text/css', href='styles.css')
    <link rel="stylesheet" type="text/css" href="styles.css">
    """
    def __new__(cls, rel=None, type=None, href=None, sizes=None, hreflang=None,
                 media=None, crossorigin=None, ):
        if isinstance(sizes, (tuple, list)):
            sizes = '{}x{}'.format(sizes[0], sizes[1])
        self = super(Link, cls).__new__(cls, **locals())
        return self
        
    def __init__(self, rel=None, type=None, href=None, sizes=None, hreflang=None,
                 media=None, crossorigin=None, ):
        if isinstance(sizes, (tuple, list)):
            sizes = '{}x{}'.format(sizes[0], sizes[1])
        _init_names(self, locals())



'''# these are not fully supported yet
class Picture(ElemContainer):
    """
    can contain source and img tags, 
    if source condition is false, skips and uses img instead
    """
class Source(Elem):
    def __init__(self, srcset='', media=None, type=None):
        if type and media:
            raise ValueError('must select either type or media, not both')
        init_names(self, locals())
'''
class Img(Elem):
    def __init__(self, src, alt=None, height=None, width=None, crossorigin=None,
                 ismap=None, longdesc=None, usemap=None):
        for name, value in locals().items():
            if value is not None and name != 'self':
                setattr(self, name, value)
Image = Img

class Map(ElemContainer): 
    """name is image's usemap value, contains Area() objects
    May be better to have this generated by gimp(?) or another program.
    Or perhaps embed svg on the DOM.
    """
    def __init__(self, elems=[], name=''):
        self.elems=elems
        self.name=name

class Area(Elem):
    """contained by Map() objects, 
    if shape is default, whole image's rectangle is map area
    if shape is circle, coords is x,y,radius
    if shape is rect, coords are x1,y1,x2,y2 (top-left to bottom right)
    if shape is poly, xi,yi,xi+1,yi+1 etc...
    """
    def __init__(self, shape='', coords=(), alt='', href=''):
        if isinstance(coords, (list, tuple)):
            coords = ','.join([str(coord) for coord in coords])
        _init_names(self, locals())
        

class Body(ElemContainer): """doc Body objects"""
class Header(ElemContainer): """"""
class Nav(ElemContainer): """"""
class Article(ElemContainer): 
    """
    Independent, self-contained content.
    Could be forum post, blog post, news story, comment.
    """
class Section(ElemContainer): """"""
class Aside(ElemContainer): 
    """
    could be sidebar, should relate to surrounding content (footnote-ish?)
    Or lift-out/callout quote from article
    """
class Footer(ElemContainer): """"""
class P(ElemContainer): """Paragraph element"""
Paragraph = P

class Address(ElemContainer):
    """
    for body, typically goes in footer, semantically the contact info for document
    for article, contact info for article
    typically separate lines with Br()/<br>
    """

class Blockquote(ElemContainer):
    """Use when quoting another source. cite is an url"""
    def __new__(cls, elems, cite=None):
        elems = elems
        return super(Blockquote, cls).__new__(cls, elems, cite=cite)
        
class Q(ElemContainer):
    """Use to quote inline"""
QuoteInline = Q

class Abbr(ElemContainer):
    """Abbreviate with mousover to expand"""
    def __new__(cls, abbr, title=''):
        elems = [abbr]
        return super(Abbr, cls).__new__(cls, elems, title=title)

class Br(Elem):
    """line break, don't use to separate paragraphs, just break lines
    for example, for poems or addresses
    """
LineBreak = Br

class OL(ElemContainer):
    """Contains list items"""
OrderedList = OL

class UL(ElemContainer):
    """Contains list items"""
UnorderedList = UL

class LI(ElemContainer):
    """LI(HyperLink(...) or whatever)"""
ListItem = LI

class A(ElemContainer):
    """
    
    """    
    def __new__(cls, href, text, target=None, ):
        kwargs = {}
        kwargs['href'] = href
        if target is not None:
            kwargs['target'] = target
        return super(A, cls).__new__(cls, text, **kwargs)

HyperLink = A
Anchor = A



def EmailLink(email_address, text=None):
    return A('mailto:' + email_address, text or email_address)


class Details(): pass #XXX


class Canvas(ElemContainer):
    """Canvas(id='myid', width='300', height='200', style='')"""
    def __init__(self, elems=[], id='', width='', height='', style=''):
        _init_names(self, locals())

class SVG(ElemContainer):
    """not really implemented, elems could be svg code? these seem to already exist"""

class Circle(Elem):
    """cx, cy, r, stroke, stroke-width, fill"""

class Audio(ElemContainer):
    """get docs"""

class Embed(ElemContainer):
    """get docs"""

class Source(Elem):
    """get docs, mostly src='something.mp3/4', 
    type='video/ogg' or 'video/webm' or 'video/mp4' or audio/ogg or audio/mpeg
        complete list: http://www.iana.org/assignments/media-types/media-types.xhtml
    media=media query e.g. "screen and (min-width:320px)"
        see http://www.w3schools.com/tags/att_source_media.asp
    """

class Track(Elem):
    """text tracks to play
    src='something.vtt'
    kind='subtitles' or chapters, descriptions, metadata, subtitles
    srclang='en' or e.g. 'no', required if subtitles
    label='text'
    bool: default 
    """

class Video(ElemContainer):
    """elems are fallback content ('your browser no support'), unless Source
    src=path.mp4 - or use a Source element. 
    width & Height
    bool: controls, autoplay, loop, muted, 
    fallback example, 1, 2, 3, 4:
    e.g. <video>
    <source src="movie.mp4">
    <source src="movie.ogv">
    <object data="movie.swf">
    <a href="movie.mp4">download</a></object></video>
    """


def writeout(htmlobjs, name='output.html'):
    """given htmlobjs, write to file with path, name=arg"""
    with open(name, 'w') as file:
        file.write(str(htmlobjs))


#if __name__ == '__main__':
#    import __main__
#    __main__.main()

'''<!DOCTYPE html>
<html lang="en">
<head><title>My Webpage</title></head>
<body>
    <ul id="navigation">
    {% for item in navigation %}
        <li><a href="{{ item.href }}">{{ item.caption }}</a></li>
    {% endfor %}
    </ul>
    <h1>My Webpage</h1>
    {{ a_variable }}
    {# a comment #}
</body>
</html>'''
