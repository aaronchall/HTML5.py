"""
Forms module, expect to provide lots of convenience functions to create Input objects
with specific documentation
"""
from __future__ import division, absolute_import, print_function

from document import Elem, ElemContainer, _init_names

class Form(ElemContainer):
    """
    takes inputs and other elems/text (maybe labels of inputs)
    
    typical keyword arguments are action, autocomplete, and novalidate

    autocomplete is 'on' or 'off'
    method e.g. 'post'
    """
    def __init__(self, elems=[], action=None, autocomplete=None, novalidate=False):
                 
        _init_names(self, locals())


class Input(Elem):
    """
    | type and name are typical arguments, note where types not implemented, typically
    interpreted as plain text, so *should* be ok to use all of these.
    | type:

    - text (name=anything)
    - password (name=psw)
    - submit (typical value: Submit)
    - image: also include alt="submit", src, height, and width (see below)
    - radio (multiple tags, same names, different values, first may be checked=True)
    - checkbox (multiple tags, different names, different values)
    - button (onclick=javascript, value=label)
    - color (name)
    - date (name, max or min in iso, ie, YYYY-MM-DD)
    - datetime (not in html5)
    - datetime-local (not in FF or IE)
    - email (name='email')
    - file (alluded to)
    - month (name, (not in FireFox or IE))
    - number (name, min, max)
    - range (name, min, max, step (optional) - should get a slider)
    - search (only in Safari and Chrome) 
    - tel (only in Safari)
    - time (not in FF or IE)
    - url (not in Safari, should add .com to keyboard)
    - week (name, not in Firefox or IE too)

    | list : (no type specified), list='mylist', define Datalist w/ id='mylist', and options
    | value, default 
    | placeholder (sample text, not default)
    | maxlength : int - limit number of characters
    | max or min : value of input field
    | pattern : regular expression to check, e.g. "[A-Za-z]{3}"
    | size : width in characters of input field
    | step : legal number intervals
    | autocomplete : off or on
    | form : specify id of form(s space separated) inputs apply to
    | formaction : override action on form
    | formenctype : e.g. "multipart/form-data" with form w/ method="post"
    | formmethod : overrides method on form e.g. second submit (or image) w/ form method="get"
    | formnovalidate : override novalidate of form, use w/ type submit
    | formtarget : overrides target,  use w/ types submit and image
    | height and width : use with type image, 
    | boolean arguments:

    - disabled, value/text can't be copied, greyed out
    - readonly, value/text can be copied
    - required, must be filled out
    - multiple, works on types email and file, accepts multiple values
    - autofocus, 
    """
    def __init__(self, type='text', name='', value='', size=None, disabled=False,
                 maxlength=None, readonly=None, autocomplete=None,
                 autofocus=False):
        _init_names(self, locals())
        '''the following are attributes for <input>
        form
        formaction
        formenctype
        formmethod
        formnovalidate
        formtarget
        height and width
        list
        min and max
        multiple
        pattern (regexp)
        placeholder
        required
        step
        '''

class Datalist(ElemContainer):
    """
    elems should be Option elements, probably goes inside Form, 
    id=list attr on Input
    """

class Option(Elem):
    """only kwarg should be value"""
