"""
This type stub file was generated by pyright.
"""

def get_locale(name):
    '''Returns an appropriate :class:`Locale <arrow.locales.Locale>`
    corresponding to an inpute locale name.

    :param name: the name of the locale.

    '''
    ...

class Locale(object):
    ''' Represents locale-specific data and functionality. '''
    names = ...
    timeframes = ...
    meridians = ...
    past = ...
    future = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    ordinal_day_re = ...
    def __init__(self):
        ...
    
    def describe(self, timeframe, delta=..., only_distance: bool = ...):
        ''' Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''
        ...
    
    def day_name(self, day):
        ''' Returns the day name for a specified day of the week.

        :param day: the ``int`` day of the week (1-7).

        '''
        ...
    
    def day_abbreviation(self, day):
        ''' Returns the day abbreviation for a specified day of the week.

        :param day: the ``int`` day of the week (1-7).

        '''
        ...
    
    def month_name(self, month):
        ''' Returns the month name for a specified month of the year.

        :param month: the ``int`` month of the year (1-12).

        '''
        ...
    
    def month_abbreviation(self, month):
        ''' Returns the month abbreviation for a specified month of the year.

        :param month: the ``int`` month of the year (1-12).

        '''
        ...
    
    def month_number(self, name):
        ''' Returns the month number for a month specified by name or abbreviation.

        :param name: the month name or abbreviation.

        '''
        ...
    
    def year_full(self, year):
        '''  Returns the year for specific locale if available

        :param name: the ``int`` year (4-digit)
        '''
        ...
    
    def year_abbreviation(self, year):
        ''' Returns the year for specific locale if available

        :param name: the ``int`` year (4-digit)
        '''
        ...
    
    def meridian(self, hour, token):
        ''' Returns the meridian indicator for a specified hour and format token.

        :param hour: the ``int`` hour of the day.
        :param token: the format token.
        '''
        ...
    
    def ordinal_number(self, n):
        ''' Returns the ordinal format of a given integer

        :param n: an integer
        '''
        ...
    
    def _ordinal_number(self, n):
        ...
    
    def _name_to_ordinal(self, lst):
        ...
    
    def _format_timeframe(self, timeframe, delta):
        ...
    
    def _format_relative(self, humanized, timeframe, delta):
        ...
    


class EnglishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    ordinal_day_re = ...
    def _ordinal_number(self, n):
        ...
    
    def describe(self, timeframe, delta=..., only_distance: bool = ...):
        ''' Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''
        ...
    


class ItalianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    ordinal_day_re = ...
    def _ordinal_number(self, n):
        ...
    


class SpanishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    ordinal_day_re = ...
    def _ordinal_number(self, n):
        ...
    


class FrenchLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    ordinal_day_re = ...
    def _ordinal_number(self, n):
        ...
    


class GreekLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class JapaneseLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class SwedishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class FinnishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        ...
    
    def _format_relative(self, humanized, timeframe, delta):
        ...
    
    def _ordinal_number(self, n):
        ...
    


class ChineseCNLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class ChineseTWLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class KoreanLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class DutchLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class SlavicBaseLocale(Locale):
    def _format_timeframe(self, timeframe, delta):
        ...
    


class BelarusianLocale(SlavicBaseLocale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class PolishLocale(SlavicBaseLocale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class RussianLocale(SlavicBaseLocale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class BulgarianLocale(SlavicBaseLocale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class UkrainianLocale(SlavicBaseLocale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class _DeutschLocaleCommonMixin(object):
    past = ...
    future = ...
    timeframes = ...
    timeframes_only_distance = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _ordinal_number(self, n):
        ...
    
    def describe(self, timeframe, delta=..., only_distance: bool = ...):
        ''' Describes a delta within a timeframe in plain language.

        :param timeframe: a string representing a timeframe.
        :param delta: a quantity representing a delta in a timeframe.
        :param only_distance: return only distance eg: "11 seconds" without "in" or "ago" keywords
        '''
        ...
    


class GermanLocale(_DeutschLocaleCommonMixin, Locale):
    names = ...


class AustrianLocale(_DeutschLocaleCommonMixin, Locale):
    names = ...
    month_names = ...


class NorwegianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class NewNorwegianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class PortugueseLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class BrazilianPortugueseLocale(PortugueseLocale):
    names = ...
    past = ...


class TagalogLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _ordinal_number(self, n):
        ...
    


class VietnameseLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class TurkishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class AzerbaijaniLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class ArabicLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        ...
    


class LevantArabicLocale(ArabicLocale):
    names = ...
    month_names = ...
    month_abbreviations = ...


class AlgeriaTunisiaArabicLocale(ArabicLocale):
    names = ...
    month_names = ...
    month_abbreviations = ...


class MauritaniaArabicLocale(ArabicLocale):
    names = ...
    month_names = ...
    month_abbreviations = ...


class MoroccoArabicLocale(ArabicLocale):
    names = ...
    month_names = ...
    month_abbreviations = ...


class IcelandicLocale(Locale):
    def _format_timeframe(self, timeframe, delta):
        ...
    
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class DanishLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class MalayalamLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class HindiLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class CzechLocale(Locale):
    names = ...
    timeframes = ...
    past = ...
    future = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        '''Czech aware time frame format function, takes into account
        the differences between past and future forms.'''
        ...
    


class SlovakLocale(Locale):
    names = ...
    timeframes = ...
    past = ...
    future = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        '''Slovak aware time frame format function, takes into account
        the differences between past and future forms.'''
        ...
    


class FarsiLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class MacedonianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class HebrewLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        '''Hebrew couple of <timeframe> aware'''
        ...
    


class MarathiLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


def _map_locales():
    ...

class CatalanLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class BasqueLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class HungarianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    meridians = ...
    def _format_timeframe(self, timeframe, delta):
        ...
    


class EsperantoLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    meridians = ...
    ordinal_day_re = ...
    def _ordinal_number(self, n):
        ...
    


class ThaiLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    meridians = ...
    BE_OFFSET = ...
    def year_full(self, year):
        '''Thai always use Buddhist Era (BE) which is CE + 543'''
        ...
    
    def year_abbreviation(self, year):
        '''Thai always use Buddhist Era (BE) which is CE + 543'''
        ...
    
    def _format_relative(self, humanized, timeframe, delta):
        '''Thai normally doesn't have any space between words'''
        ...
    


class BengaliLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _ordinal_number(self, n):
        ...
    


class RomanshLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class SwissLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class RomanianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class SlovenianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class IndonesianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class NepaliLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    meridians = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...


class EstonianLocale(Locale):
    names = ...
    past = ...
    future = ...
    timeframes = ...
    month_names = ...
    month_abbreviations = ...
    day_names = ...
    day_abbreviations = ...
    def _format_timeframe(self, timeframe, delta):
        ...
    


_locales = _map_locales()
