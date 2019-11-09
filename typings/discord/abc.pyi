"""
This type stub file was generated by pyright.
"""

import abc
from collections import namedtuple
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
class _Undefined:
    def __repr__(self):
        ...
    


_undefined = _Undefined()
class Snowflake(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a Discord model.

    Almost all :ref:`Discord models <discord_api_models>` meet this
    abstract base class.

    Attributes
    -----------
    id: :class:`int`
        The model's unique ID.
    """
    __slots__ = ...
    @property
    @abc.abstractmethod
    def created_at(self):
        """:class:`datetime.datetime`: Returns the model's creation time as a naive datetime in UTC."""
        ...
    
    @classmethod
    def __subclasshook__(cls, C):
        ...
    


class User(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a Discord user.

    The following implement this ABC:

    - :class:`~discord.User`
    - :class:`~discord.ClientUser`
    - :class:`~discord.Member`

    This ABC must also implement :class:`~discord.abc.Snowflake`.

    Attributes
    -----------
    name: :class:`str`
        The user's username.
    discriminator: :class:`str`
        The user's discriminator.
    avatar: Optional[:class:`str`]
        The avatar hash the user has.
    bot: :class:`bool`
        If the user is a bot account.
    """
    __slots__ = ...
    @property
    @abc.abstractmethod
    def display_name(self):
        """:class:`str`: Returns the user's display name."""
        ...
    
    @property
    @abc.abstractmethod
    def mention(self):
        """:class:`str`: Returns a string that allows you to mention the given user."""
        ...
    
    @classmethod
    def __subclasshook__(cls, C):
        ...
    


class PrivateChannel(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a private Discord channel.

    The following implement this ABC:

    - :class:`~discord.DMChannel`
    - :class:`~discord.GroupChannel`

    This ABC must also implement :class:`~discord.abc.Snowflake`.

    Attributes
    -----------
    me: :class:`~discord.ClientUser`
        The user presenting yourself.
    """
    __slots__ = ...
    @classmethod
    def __subclasshook__(cls, C):
        ...
    


_Overwrites = namedtuple('_Overwrites', 'id allow deny type')
class GuildChannel:
    """An ABC that details the common operations on a Discord guild channel.

    The following implement this ABC:

    - :class:`~discord.TextChannel`
    - :class:`~discord.VoiceChannel`
    - :class:`~discord.CategoryChannel`

    This ABC must also implement :class:`~discord.abc.Snowflake`.

    Attributes
    -----------
    name: :class:`str`
        The channel name.
    guild: :class:`~discord.Guild`
        The guild the channel belongs to.
    position: :class:`int`
        The position in the channel list. This is a number that starts at 0.
        e.g. the top channel is position 0.
    """
    __slots__ = ...
    def __str__(self):
        ...
    
    @property
    def _sorting_bucket(self):
        ...
    
    async def _move(self, position, parent_id: Optional[Any] = ..., lock_permissions: bool = ..., *, reason):
        self.position = ...
    
    async def _edit(self, options, reason):
        ...
    
    def _fill_overwrites(self, data):
        ...
    
    @property
    def changed_roles(self):
        """List[:class:`~discord.Role`]: Returns a list of roles that have been overridden from
        their default values in the :attr:`~discord.Guild.roles` attribute."""
        ...
    
    @property
    def mention(self):
        """:class:`str`: The string that allows you to mention the channel."""
        ...
    
    @property
    def created_at(self):
        """:class:`datetime.datetime`: Returns the channel's creation time in UTC."""
        ...
    
    def overwrites_for(self, obj):
        """Returns the channel-specific overwrites for a member or a role.

        Parameters
        -----------
        obj: Union[:class:`~discord.Role`, :class:`~discord.abc.User`]
            The role or user denoting
            whose overwrite to get.

        Returns
        ---------
        :class:`~discord.PermissionOverwrite`
            The permission overwrites for this object.
        """
        ...
    
    @property
    def overwrites(self):
        """Returns all of the channel's overwrites.

        This is returned as a dictionary where the key contains the target which
        can be either a :class:`~discord.Role` or a :class:`~discord.Member` and the key is the
        overwrite as a :class:`~discord.PermissionOverwrite`.

        Returns
        --------
        Mapping[Union[:class:`~discord.Role`, :class:`~discord.Member`], :class:`~discord.PermissionOverwrite`]
            The channel's permission overwrites.
        """
        ...
    
    @property
    def category(self):
        """Optional[:class:`~discord.CategoryChannel`]: The category this channel belongs to.

        If there is no category then this is ``None``.
        """
        ...
    
    def permissions_for(self, member):
        """Handles permission resolution for the current :class:`~discord.Member`.

        This function takes into consideration the following cases:

        - Guild owner
        - Guild roles
        - Channel overrides
        - Member overrides

        Parameters
        ----------
        member: :class:`~discord.Member`
            The member to resolve permissions for.

        Returns
        -------
        :class:`~discord.Permissions`
            The resolved permissions for the member.
        """
        ...
    
    async def delete(self, *, reason: Optional[Any] = ...):
        """|coro|

        Deletes the channel.

        You must have :attr:`~.Permissions.manage_channels` permission to use this.

        Parameters
        -----------
        reason: Optional[:class:`str`]
            The reason for deleting this channel.
            Shows up on the audit log.

        Raises
        -------
        :exc:`~discord.Forbidden`
            You do not have proper permissions to delete the channel.
        :exc:`~discord.NotFound`
            The channel was not found or was already deleted.
        :exc:`~discord.HTTPException`
            Deleting the channel failed.
        """
        ...
    
    async def set_permissions(self, target, *, overwrite=..., reason: Optional[Any] = ..., **permissions):
        r"""|coro|

        Sets the channel specific permission overwrites for a target in the
        channel.

        The ``target`` parameter should either be a :class:`~discord.Member` or a
        :class:`~discord.Role` that belongs to guild.

        The ``overwrite`` parameter, if given, must either be ``None`` or
        :class:`~discord.PermissionOverwrite`. For convenience, you can pass in
        keyword arguments denoting :class:`~discord.Permissions` attributes. If this is
        done, then you cannot mix the keyword arguments with the ``overwrite``
        parameter.

        If the ``overwrite`` parameter is ``None``, then the permission
        overwrites are deleted.

        You must have the :attr:`~.Permissions.manage_roles` permission to use this.

        Examples
        ----------

        Setting allow and deny: ::

            await message.channel.set_permissions(message.author, read_messages=True,
                                                                  send_messages=False)

        Deleting overwrites ::

            await channel.set_permissions(member, overwrite=None)

        Using :class:`~discord.PermissionOverwrite` ::

            overwrite = discord.PermissionOverwrite()
            overwrite.send_messages = False
            overwrite.read_messages = True
            await channel.set_permissions(member, overwrite=overwrite)

        Parameters
        -----------
        target: Union[:class:`~discord.Member`, :class:`~discord.Role`]
            The member or role to overwrite permissions for.
        overwrite: :class:`~discord.PermissionOverwrite`
            The permissions to allow and deny to the target.
        \*\*permissions
            A keyword argument list of permissions to set for ease of use.
            Cannot be mixed with ``overwrite``.
        reason: Optional[:class:`str`]
            The reason for doing this action. Shows up on the audit log.

        Raises
        -------
        :exc:`~discord.Forbidden`
            You do not have permissions to edit channel specific permissions.
        :exc:`~discord.HTTPException`
            Editing channel specific permissions failed.
        :exc:`~discord.NotFound`
            The role or member being edited is not part of the guild.
        :exc:`~discord.InvalidArgument`
            The overwrite parameter invalid or the target type was not
            :class:`~discord.Role` or :class:`~discord.Member`.
        """
        ...
    
    async def _clone_impl(self, base_attrs, *, name: Optional[Any] = ..., reason: Optional[Any] = ...):
        ...
    
    async def clone(self, *, name: Optional[Any] = ..., reason: Optional[Any] = ...):
        """|coro|

        Clones this channel. This creates a channel with the same properties
        as this channel.

        .. versionadded:: 1.1.0

        Parameters
        ------------
        name: Optional[:class:`str`]
            The name of the new channel. If not provided, defaults to this
            channel name.
        reason: Optional[:class:`str`]
            The reason for cloning this channel. Shows up on the audit log.

        Raises
        -------
        :exc:`~discord.Forbidden`
            You do not have the proper permissions to create this channel.
        :exc:`~discord.HTTPException`
            Creating the channel failed.
        """
        ...
    
    async def create_invite(self, *, reason: Optional[Any] = ..., **fields):
        """|coro|

        Creates an instant invite.

        You must have the :attr:`~.Permissions.create_instant_invite` permission to
        do this.

        Parameters
        ------------
        max_age: :class:`int`
            How long the invite should last. If it's 0 then the invite
            doesn't expire. Defaults to 0.
        max_uses: :class:`int`
            How many uses the invite could be used for. If it's 0 then there
            are unlimited uses. Defaults to 0.
        temporary: :class:`bool`
            Denotes that the invite grants temporary membership
            (i.e. they get kicked after they disconnect). Defaults to ``False``.
        unique: :class:`bool`
            Indicates if a unique invite URL should be created. Defaults to True.
            If this is set to ``False`` then it will return a previously created
            invite.
        reason: Optional[:class:`str`]
            The reason for creating this invite. Shows up on the audit log.

        Raises
        -------
        :exc:`~discord.HTTPException`
            Invite creation failed.

        Returns
        --------
        :class:`~discord.Invite`
            The invite that was created.
        """
        ...
    
    async def invites(self):
        """|coro|

        Returns a list of all active instant invites from this channel.

        You must have :attr:`~.Permissions.manage_guild` to get this information.

        Raises
        -------
        :exc:`~discord.Forbidden`
            You do not have proper permissions to get the information.
        :exc:`~discord.HTTPException`
            An error occurred while fetching the information.

        Returns
        -------
        List[:class:`~discord.Invite`]
            The list of invites that are currently active.
        """
        ...
    


class Messageable(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a model that can send messages.

    The following implement this ABC:

    - :class:`~discord.TextChannel`
    - :class:`~discord.DMChannel`
    - :class:`~discord.GroupChannel`
    - :class:`~discord.User`
    - :class:`~discord.Member`
    - :class:`~discord.ext.commands.Context`

    This ABC must also implement :class:`~discord.abc.Snowflake`.
    """
    __slots__ = ...
    @abc.abstractmethod
    async def _get_channel(self):
        ...
    
    async def send(self, content: Optional[Any] = ..., *, tts: bool = ..., embed: Optional[Any] = ..., file: Optional[Any] = ..., files: Optional[Any] = ..., delete_after: Optional[Any] = ..., nonce: Optional[Any] = ...):
        """|coro|

        Sends a message to the destination with the content given.

        The content must be a type that can convert to a string through ``str(content)``.
        If the content is set to ``None`` (the default), then the ``embed`` parameter must
        be provided.

        To upload a single file, the ``file`` parameter should be used with a
        single :class:`~discord.File` object. To upload multiple files, the ``files``
        parameter should be used with a :class:`list` of :class:`~discord.File` objects.
        **Specifying both parameters will lead to an exception**.

        If the ``embed`` parameter is provided, it must be of type :class:`~discord.Embed` and
        it must be a rich embed type.

        Parameters
        ------------
        content: :class:`str`
            The content of the message to send.
        tts: :class:`bool`
            Indicates if the message should be sent using text-to-speech.
        embed: :class:`~discord.Embed`
            The rich embed for the content.
        file: :class:`~discord.File`
            The file to upload.
        files: List[:class:`~discord.File`]
            A list of files to upload. Must be a maximum of 10.
        nonce: :class:`int`
            The nonce to use for sending this message. If the message was successfully sent,
            then the message will have a nonce with this value.
        delete_after: :class:`float`
            If provided, the number of seconds to wait in the background
            before deleting the message we just sent. If the deletion fails,
            then it is silently ignored.

        Raises
        --------
        :exc:`~discord.HTTPException`
            Sending the message failed.
        :exc:`~discord.Forbidden`
            You do not have the proper permissions to send the message.
        :exc:`~discord.InvalidArgument`
            The ``files`` list is not of the appropriate size or
            you specified both ``file`` and ``files``.

        Returns
        ---------
        :class:`~discord.Message`
            The message that was sent.
        """
        ...
    
    async def trigger_typing(self):
        """|coro|

        Triggers a *typing* indicator to the destination.

        *Typing* indicator will go away after 10 seconds, or after a message is sent.
        """
        ...
    
    def typing(self):
        """Returns a context manager that allows you to type for an indefinite period of time.

        This is useful for denoting long computations in your bot.

        .. note::

            This is both a regular context manager and an async context manager.
            This means that both ``with`` and ``async with`` work with this.

        Example Usage: ::

            async with channel.typing():
                # do expensive stuff here
                await channel.send('done!')

        """
        ...
    
    async def fetch_message(self, id):
        """|coro|

        Retrieves a single :class:`~discord.Message` from the destination.

        This can only be used by bot accounts.

        Parameters
        ------------
        id: :class:`int`
            The message ID to look for.

        Raises
        --------
        :exc:`~discord.NotFound`
            The specified message was not found.
        :exc:`~discord.Forbidden`
            You do not have the permissions required to get a message.
        :exc:`~discord.HTTPException`
            Retrieving the message failed.

        Returns
        --------
        :class:`~discord.Message`
            The message asked for.
        """
        ...
    
    async def pins(self):
        """|coro|

        Retrieves all messages that are currently pinned in the channel.

        .. note::

            Due to a limitation with the Discord API, the :class:`.Message`
            objects returned by this method do not contain complete
            :attr:`.Message.reactions` data.

        Raises
        -------
        :exc:`~discord.HTTPException`
            Retrieving the pinned messages failed.

        Returns
        --------
        List[:class:`~discord.Message`]
            The messages that are currently pinned.
        """
        ...
    
    def history(self, *, limit=..., before: Optional[Any] = ..., after: Optional[Any] = ..., around: Optional[Any] = ..., oldest_first: Optional[Any] = ...):
        """Returns an :class:`~discord.AsyncIterator` that enables receiving the destination's message history.

        You must have :attr:`~.Permissions.read_message_history` permissions to use this.

        Examples
        ---------

        Usage ::

            counter = 0
            async for message in channel.history(limit=200):
                if message.author == client.user:
                    counter += 1

        Flattening into a list: ::

            messages = await channel.history(limit=123).flatten()
            # messages is now a list of Message...

        All parameters are optional.

        Parameters
        -----------
        limit: Optional[:class:`int`]
            The number of messages to retrieve.
            If ``None``, retrieves every message in the channel. Note, however,
            that this would make it a slow operation.
        before: Optional[Union[:class:`~discord.abc.Snowflake`, :class:`datetime.datetime`]]
            Retrieve messages before this date or message.
            If a date is provided it must be a timezone-naive datetime representing UTC time.
        after: Optional[Union[:class:`~discord.abc.Snowflake`, :class:`datetime.datetime`]]
            Retrieve messages after this date or message.
            If a date is provided it must be a timezone-naive datetime representing UTC time.
        around: Optional[Union[:class:`~discord.abc.Snowflake`, :class:`datetime.datetime`]]
            Retrieve messages around this date or message.
            If a date is provided it must be a timezone-naive datetime representing UTC time.
            When using this argument, the maximum limit is 101. Note that if the limit is an
            even number then this will return at most limit + 1 messages.
        oldest_first: Optional[:class:`bool`]
            If set to ``True``, return messages in oldest->newest order. Defaults to ``True`` if
            ``after`` is specified, otherwise ``False``.

        Raises
        ------
        :exc:`~discord.Forbidden`
            You do not have permissions to get channel message history.
        :exc:`~discord.HTTPException`
            The request to get message history failed.

        Yields
        -------
        :class:`~discord.Message`
            The message with the message data parsed.
        """
        ...
    


class Connectable(metaclass=abc.ABCMeta):
    """An ABC that details the common operations on a channel that can
    connect to a voice server.

    The following implement this ABC:

    - :class:`~discord.VoiceChannel`
    """
    __slots__ = ...
    @abc.abstractmethod
    def _get_voice_client_key(self):
        ...
    
    @abc.abstractmethod
    def _get_voice_state_pair(self):
        ...
    
    async def connect(self, *, timeout=..., reconnect: bool = ...):
        """|coro|

        Connects to voice and creates a :class:`VoiceClient` to establish
        your connection to the voice server.

        Parameters
        -----------
        timeout: :class:`float`
            The timeout in seconds to wait for the voice endpoint.
        reconnect: :class:`bool`
            Whether the bot should automatically attempt
            a reconnect if a part of the handshake fails
            or the gateway goes down.

        Raises
        -------
        :exc:`asyncio.TimeoutError`
            Could not connect to the voice channel in time.
        :exc:`~discord.ClientException`
            You are already connected to a voice channel.
        :exc:`~discord.opus.OpusNotLoaded`
            The opus library has not been loaded.

        Returns
        --------
        :class:`~discord.VoiceClient`
            A voice client that is fully connected to the voice server.
        """
        ...
    

