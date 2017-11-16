from setuptools import setup, find_packages
import os.path as _op

NAME = 'html5.py'

# can be rst: maybe should use same text as README.rst?
with open(_op.join(_op.abspath(_op.dirname(__file__)), 'README.rst')) as f:
    LONGDESCRIPTION = f.read()


# below gleaned from https://pypi.python.org/pypi?%3Aaction=list_classifiers
# maybe some are redundant or inaccurate?
CLASSIFIERS = """Development Status :: 2 - Pre-Alpha
Environment :: Console
Environment :: Web Environment
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: End Users/Desktop
Intended Audience :: Information Technology
Intended Audience :: System Administrators
License :: OSI Approved
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 2.6
Programming Language :: Python :: 2.7
Programming Language :: Python :: 3
Programming Language :: Python :: 3.1
Programming Language :: Python :: 3.2
Programming Language :: Python :: 3.3
Programming Language :: Python :: 3.4
Programming Language :: Python :: 3.5
Topic :: Documentation
Topic :: Internet
Topic :: Internet :: WWW/HTTP
Topic :: Internet :: WWW/HTTP :: Browsers
Topic :: Internet :: WWW/HTTP :: Dynamic Content
Topic :: Internet :: WWW/HTTP :: Indexing/Search
Topic :: Internet :: WWW/HTTP :: Site Management
Topic :: Software Development
Topic :: Software Development :: Build Tools
Topic :: Software Development :: Code Generators
Topic :: Software Development :: Documentation
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Topic :: Software Development :: Pre-processors
Topic :: Text Editors
Topic :: Text Editors :: Text Processing
Topic :: Text Processing
Topic :: Text Processing :: Markup
Topic :: Text Processing :: Markup :: HTML
Topic :: Utilities""".splitlines()

PACKAGES = ['html5'] # find_packages(where='html5')
print(PACKAGES)
NAME = 'Aaron Hall'
EMAIL = 'aaronchall@yahoo.com'
KEYWORDS = ['HTML5', 'Documentation', 'library']
VERSION = open(_op.join(_op.abspath(_op.dirname(__file__)), 'html5', 'VERSION')).read()
print(VERSION)

setup(
    name=NAME,
    version=open('html5/VERSION').read().strip(),
    description='HTML5 library',
    author=NAME,
    author_email=EMAIL,
    maintainer=NAME,
    maintainer_email=EMAIL,
    url='http://www.github.com/aaronchall/html5.py',
    long_description=LONGDESCRIPTION,
    classifiers=CLASSIFIERS,
    install_requires=[],
    zip_safe=True
)
