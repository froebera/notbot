"""
This type stub file was generated by pyright.
"""

class DateTimeFormatter(object):
    _FORMAT_RE = ...
    def __init__(self, locale=...):
        self.locale = ...
    
    def format(cls, dt, fmt):
        ...
    
    def _format_token(self, dt, token):
        ...
    

