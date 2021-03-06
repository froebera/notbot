"""
This type stub file was generated by pyright.
"""

import sys

def total_seconds(td):
    ...

def is_timestamp(value):
    ...

class list_to_iter_shim(list):
    ''' A temporary shim for functions that currently return a list but that will, after a
    deprecation period, return an iteratator.
    '''
    def __init__(self, iterable=..., **kwargs):
        ''' Equivalent to list(iterable).  warn_text will be emitted on all non-iterator operations.
        '''
        ...
    
    def _warn(self):
        ...
    
    def __iter__(self):
        ...
    
    def _wrap_method(name):
        ...
    
    __contains__ = ...
    __add__ = ...
    __mul__ = ...
    __getitem__ = ...
    index = ...
    count = ...
    __setitem__ = ...
    __delitem__ = ...
    append = ...
    if sys.version_info.major >= 3:
        clear = ...
        copy = ...
    extend = ...
    __iadd__ = ...
    __imul__ = ...
    insert = ...
    pop = ...
    remove = ...
    reverse = ...
    sort = ...


__all__ = ['total_seconds', 'is_timestamp', 'isstr', 'list_to_iter_shim', 'list_to_iter_deprecation']
