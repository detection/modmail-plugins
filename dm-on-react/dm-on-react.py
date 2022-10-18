import asyncio
import emoji
import re
import typing
import logging

import discord
from discord.ext import commands

logger = logging.getLogger("Modmail")

from core import checks
from core.models import PermissionLevel

class UnicodeEmoji(commands.Converter):
    async def convert(self, ctx, argument):
        if argument in emoji.UNICODE_EMOJI:
            return discord.PartialEmoji(name=argument, animated=False)
        raise commands.BadArgument('Unknown emoji')

Emoji = typing.Union[discord.PartialEmoji, discord.Emoji, UnicodeEmoji]

class DmOnReactPlugin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.group(name="dmonreact", aliases=["dmr"], invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def dmonreact(self, ctx: commands.Context):
        """Send a DM to a user on reaction"""
        await ctx.send_help(ctx.command)

    @dmonreact.command(name="add", aliases=["make"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def dmr_add(self, ctx, message: str, emoji: Emoji,
                     ignored_roles: commands.Greedy[discord.Role] = None):
        """
        Sets up the message users will react to.
        - Note(s):
        You can only use the emoji once, you can't use the emoji multiple times.
        """
        emote = emoji.name if emoji.id is None else str(emoji.id)
        message_id = int(message.split("/")[-1])

        for channel in ctx.guild.text_channels:
            try:
                message = await channel.fetch_message(message_id)
            except (discord.NotFound, discord.HTTPException, discord.Forbidden):
                message = None
                continue
            else:
                break

        if not message:
            return await ctx.send("Message could not be found.")

        if ignored_roles:
            blacklist = [role.id for role in ignored_roles]
        else:
            blacklist = []

        await self.db.find_one_and_update(
            {"_id": "config"}, {"$set": {emote: {"msg_id": message.id, "ignored_roles": blacklist, "state": "unlocked"}}},
            upsert=True)

        await message.add_reaction(emoji)
        await ctx.send("Successfuly set the react message!")

    @dmonreact.command(name="remove", aliases=["delete"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def dmr_remove(self, ctx, emoji: Emoji):
        """Delete something from the react DMs."""
        emote = emoji.name if emoji.id is None else str(emoji.id)
        config = await self.db.find_one({"_id": "config"})

        valid, msg = self.valid_emoji(emote, config)
        if not valid:
            return await ctx.send(msg)

        await self.db.find_one_and_update({"_id": "config"}, {"$unset": {emote: ""}})
        await ctx.send("Successfully removed the role from the reaction role.")

    @dmonreact.command(aliases=["sdm"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def setdmmsg(self, ctx, *, message):
        """Set a message to DM a user when they react"""
        if message.startswith("https://") or message.startswith("http://"):
            # message is a URL
            if message.startswith("https://hasteb.in/"):
                message = "https://hasteb.in/raw/" + message.split("/")[-1]

            async with self.bot.session.get(message) as resp:
                message = await resp.text()

        await self.db.find_one_and_update(
            {"_id": "config"},
            {"$set": {"dm-msg": {"message": message}}},
            upsert=True,
        )

        await ctx.send("Successfully set the message.")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        if not payload.guild_id:
            return
        
        config = await self.db.find_one({"_id": "config"})

        emote = payload.emoji.name if payload.emoji.id is None else str(payload.emoji.id)
        emoji = payload.emoji.name if payload.emoji.id is None else payload.emoji

        guild = self.bot.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)

        if member.bot:
            return

        try:
            msg_id = config[emote]["msg_id"]
        except (KeyError, TypeError):
            return

        if payload.message_id != int(msg_id):
            return

        if config is None:
            logger.info("User reacted, but no DM message was set.")
            return

        try:
            message = config["dm-msg"]["message"]
            await member.send(message.replace("{user}", str(member)))
            await ctx.send(message.content)
        except:
            return


async def setup(bot):
    await bot.add_cog(DmOnReactPlugin(bot))
