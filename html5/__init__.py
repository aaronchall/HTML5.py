from __future__ import division, absolute_import, print_function
from html5.document import *
from html5.forms import *

import os.path as _op


with open(_op.join(_op.abspath(_op.dirname(__file__)), 'VERSION')) as f:
    __version__ = f.read()


