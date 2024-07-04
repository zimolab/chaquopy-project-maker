"""
This file is used by pyinstaller to import hidden imports.

Some module may be imported and used in an unusual way (for example cookiecutter.extensions),
and Pyinstaller will not pack it into the final executable, so we had to manually import those modules here.
"""

from cookiecutter.exceptions import *
from cookiecutter.extensions import *
