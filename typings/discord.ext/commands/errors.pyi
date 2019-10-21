"""
This type stub file was generated by pyright.
"""

from discord.errors import DiscordException
from typing import Any, Optional

"""
The MIT License (MIT)

Copyright (c) 2015-2019 Rapptz

Permission is hereby granted, free of charge, to any person obtaining a
copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
DEALINGS IN THE SOFTWARE.
"""
__all__ = ('CommandError', 'MissingRequiredArgument', 'BadArgument', 'PrivateMessageOnly', 'NoPrivateMessage', 'CheckFailure', 'CommandNotFound', 'DisabledCommand', 'CommandInvokeError', 'TooManyArguments', 'UserInputError', 'CommandOnCooldown', 'NotOwner', 'MissingRole', 'BotMissingRole', 'MissingAnyRole', 'BotMissingAnyRole', 'MissingPermissions', 'BotMissingPermissions', 'NSFWChannelRequired', 'ConversionError', 'BadUnionArgument', 'ArgumentParsingError', 'UnexpectedQuoteError', 'InvalidEndOfQuotedStringError', 'ExpectedClosingQuoteError', 'ExtensionError', 'ExtensionAlreadyLoaded', 'ExtensionNotLoaded', 'NoEntryPointError', 'ExtensionFailed', 'ExtensionNotFound')
class CommandError(DiscordException):
    r"""The base exception type for all command related errors.

    This inherits from :exc:`discord.DiscordException`.

    This exception and exceptions inherited from it are handled
    in a special way as they are caught and passed into a special event
    from :class:`.Bot`\, :func:`on_command_error`.
    """
    def __init__(self, message: Optional[Any] = ..., *args):
        ...
    


class ConversionError(CommandError):
    """Exception raised when a Converter class raises non-CommandError.

    This inherits from :exc:`CommandError`.

    Attributes
    ----------
    converter: :class:`discord.ext.commands.Converter`
        The converter that failed.
    original
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, converter, original):
        self.converter = ...
        self.original = ...
    


class UserInputError(CommandError):
    """The base exception type for errors that involve errors
    regarding user input.

    This inherits from :exc:`CommandError`.
    """
    ...


class CommandNotFound(CommandError):
    """Exception raised when a command is attempted to be invoked
    but no command under that name is found.

    This is not raised for invalid subcommands, rather just the
    initial main command that is attempted to be invoked.

    This inherits from :exc:`CommandError`.
    """
    ...


class MissingRequiredArgument(UserInputError):
    """Exception raised when parsing a command and a parameter
    that is required is not encountered.

    This inherits from :exc:`UserInputError`

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The argument that is missing.
    """
    def __init__(self, param):
        self.param = ...
    


class TooManyArguments(UserInputError):
    """Exception raised when the command was passed too many arguments and its
    :attr:`.Command.ignore_extra` attribute was not set to ``True``.

    This inherits from :exc:`UserInputError`
    """
    ...


class BadArgument(UserInputError):
    """Exception raised when a parsing or conversion failure is encountered
    on an argument to pass into a command.

    This inherits from :exc:`UserInputError`
    """
    ...


class CheckFailure(CommandError):
    """Exception raised when the predicates in :attr:`.Command.checks` have failed.

    This inherits from :exc:`CommandError`
    """
    ...


class PrivateMessageOnly(CheckFailure):
    """Exception raised when an operation does not work outside of private
    message contexts.

    This inherits from :exc:`CheckFailure`
    """
    def __init__(self, message: Optional[Any] = ...):
        ...
    


class NoPrivateMessage(CheckFailure):
    """Exception raised when an operation does not work in private message
    contexts.

    This inherits from :exc:`CheckFailure`
    """
    def __init__(self, message: Optional[Any] = ...):
        ...
    


class NotOwner(CheckFailure):
    """Exception raised when the message author is not the owner of the bot.

    This inherits from :exc:`CheckFailure`
    """
    ...


class DisabledCommand(CommandError):
    """Exception raised when the command being invoked is disabled.

    This inherits from :exc:`CommandError`
    """
    ...


class CommandInvokeError(CommandError):
    """Exception raised when the command being invoked raised an exception.

    This inherits from :exc:`CommandError`

    Attributes
    -----------
    original
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, e):
        self.original = ...
    


class CommandOnCooldown(CommandError):
    """Exception raised when the command being invoked is on cooldown.

    This inherits from :exc:`CommandError`

    Attributes
    -----------
    cooldown: Cooldown
        A class with attributes ``rate``, ``per``, and ``type`` similar to
        the :func:`.cooldown` decorator.
    retry_after: :class:`float`
        The amount of seconds to wait before you can retry again.
    """
    def __init__(self, cooldown, retry_after):
        self.cooldown = ...
        self.retry_after = ...
    


class MissingRole(CheckFailure):
    """Exception raised when the command invoker lacks a role to run a command.

    This inherits from :exc:`CheckFailure`

    .. versionadded:: 1.1.0

    Attributes
    -----------
    missing_role: Union[:class:`str`, :class:`int`]
        The required role that is missing.
        This is the parameter passed to :func:`~.commands.has_role`.
    """
    def __init__(self, missing_role):
        self.missing_role = ...
    


class BotMissingRole(CheckFailure):
    """Exception raised when the bot's member lacks a role to run a command.

    This inherits from :exc:`CheckFailure`

    .. versionadded:: 1.1.0

    Attributes
    -----------
    missing_role: Union[:class:`str`, :class:`int`]
        The required role that is missing.
        This is the parameter passed to :func:`~.commands.has_role`.
    """
    def __init__(self, missing_role):
        self.missing_role = ...
    


class MissingAnyRole(CheckFailure):
    """Exception raised when the command invoker lacks any of
    the roles specified to run a command.

    This inherits from :exc:`CheckFailure`

    .. versionadded:: 1.1.0

    Attributes
    -----------
    missing_roles: List[Union[:class:`str`, :class:`int`]]
        The roles that the invoker is missing.
        These are the parameters passed to :func:`~.commands.has_any_role`.
    """
    def __init__(self, missing_roles):
        self.missing_roles = ...
    


class BotMissingAnyRole(CheckFailure):
    """Exception raised when the bot's member lacks any of
    the roles specified to run a command.

    This inherits from :exc:`CheckFailure`

    .. versionadded:: 1.1.0

    Attributes
    -----------
    missing_roles: List[Union[:class:`str`, :class:`int`]]
        The roles that the bot's member is missing.
        These are the parameters passed to :func:`~.commands.has_any_role`.

    """
    def __init__(self, missing_roles):
        self.missing_roles = ...
    


class NSFWChannelRequired(CheckFailure):
    """Exception raised when a channel does not have the required NSFW setting.

    This inherits from :exc:`CheckFailure`.

    .. versionadded:: 1.1.0

    Parameters
    -----------
    channel: :class:`discord.abc.GuildChannel`
        The channel that does not have NSFW enabled.
    """
    def __init__(self, channel):
        self.channel = ...
    


class MissingPermissions(CheckFailure):
    """Exception raised when the command invoker lacks permissions to run a
    command.

    This inherits from :exc:`CheckFailure`

    Attributes
    -----------
    missing_perms: :class:`list`
        The required permissions that are missing.
    """
    def __init__(self, missing_perms, *args):
        self.missing_perms = ...
    


class BotMissingPermissions(CheckFailure):
    """Exception raised when the bot's member lacks permissions to run a
    command.

    This inherits from :exc:`CheckFailure`

    Attributes
    -----------
    missing_perms: :class:`list`
        The required permissions that are missing.
    """
    def __init__(self, missing_perms, *args):
        self.missing_perms = ...
    


class BadUnionArgument(UserInputError):
    """Exception raised when a :data:`typing.Union` converter fails for all
    its associated types.

    This inherits from :exc:`UserInputError`

    Attributes
    -----------
    param: :class:`inspect.Parameter`
        The parameter that failed being converted.
    converters: Tuple[Type, ...]
        A tuple of converters attempted in conversion, in order of failure.
    errors: List[:class:`CommandError`]
        A list of errors that were caught from failing the conversion.
    """
    def __init__(self, param, converters, errors):
        self.param = ...
        self.converters = ...
        self.errors = ...
    


class ArgumentParsingError(UserInputError):
    """An exception raised when the parser fails to parse a user's input.

    This inherits from :exc:`UserInputError`.

    There are child classes that implement more granular parsing errors for
    i18n purposes.
    """
    ...


class UnexpectedQuoteError(ArgumentParsingError):
    """An exception raised when the parser encounters a quote mark inside a non-quoted string.

    This inherits from :exc:`ArgumentParsingError`.

    Attributes
    ------------
    quote: :class:`str`
        The quote mark that was found inside the non-quoted string.
    """
    def __init__(self, quote):
        self.quote = ...
    


class InvalidEndOfQuotedStringError(ArgumentParsingError):
    """An exception raised when a space is expected after the closing quote in a string
    but a different character is found.

    This inherits from :exc:`ArgumentParsingError`.

    Attributes
    -----------
    char: :class:`str`
        The character found instead of the expected string.
    """
    def __init__(self, char):
        self.char = ...
    


class ExpectedClosingQuoteError(ArgumentParsingError):
    """An exception raised when a quote character is expected but not found.

    This inherits from :exc:`ArgumentParsingError`.

    Attributes
    -----------
    close_quote: :class:`str`
        The quote character expected.
    """
    def __init__(self, close_quote):
        self.close_quote = ...
    


class ExtensionError(DiscordException):
    """Base exception for extension related errors.

    This inherits from :exc:`~discord.DiscordException`.

    Attributes
    ------------
    name: :class:`str`
        The extension that had an error.
    """
    def __init__(self, message: Optional[Any] = ..., *args, name):
        self.name = ...
    


class ExtensionAlreadyLoaded(ExtensionError):
    """An exception raised when an extension has already been loaded.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        ...
    


class ExtensionNotLoaded(ExtensionError):
    """An exception raised when an extension was not loaded.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        ...
    


class NoEntryPointError(ExtensionError):
    """An exception raised when an extension does not have a ``setup`` entry point function.

    This inherits from :exc:`ExtensionError`
    """
    def __init__(self, name):
        ...
    


class ExtensionFailed(ExtensionError):
    """An exception raised when an extension failed to load during execution of the ``setup`` entry point.

    This inherits from :exc:`ExtensionError`

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    original: :exc:`Exception`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, name, original):
        self.original = ...
    


class ExtensionNotFound(ExtensionError):
    """An exception raised when an extension failed to be imported.

    This inherits from :exc:`ExtensionError`

    Attributes
    -----------
    name: :class:`str`
        The extension that had the error.
    original: :exc:`ImportError`
        The original exception that was raised. You can also get this via
        the ``__cause__`` attribute.
    """
    def __init__(self, name, original):
        self.original = ...
    


