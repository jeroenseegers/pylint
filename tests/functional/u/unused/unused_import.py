"""unused import"""
# pylint: disable=undefined-all-variable, import-error, no-absolute-import, too-few-public-methods, missing-docstring,wrong-import-position, useless-object-inheritance, multiple-imports
import xml.etree  # [unused-import]
import xml.sax  # [unused-import]
import os.path as test  # [unused-import]
from sys import argv as test2  # [unused-import]
from sys import flags  # [unused-import]
# +1:[unused-import,unused-import]
from collections import deque, OrderedDict, Counter
import re, html.parser  # [unused-import]
DATA = Counter()
# pylint: disable=self-assigning-variable
from fake import SomeName, SomeOtherName  # [unused-import]
class SomeClass(object):
    SomeName = SomeName # https://bitbucket.org/logilab/pylint/issue/475
    SomeOtherName = 1
    SomeOtherName = SomeOtherName

from never import __all__
# pylint: disable=wrong-import-order,ungrouped-imports
import typing
from typing import TYPE_CHECKING


if typing.TYPE_CHECKING:
    import collections
if TYPE_CHECKING:
    import itertools


def get_ordered_dict() -> 'collections.OrderedDict':
    return []


def get_itertools_obj() -> 'itertools.count':
    return []

def use_html_parser() -> 'html.parser.HTMLParser':
    return html.parser.HTMLParser