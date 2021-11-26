import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class ChannelPerms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    guild = self.bot.get_guild(173554823633829888)
    Madrid = guild.get_role(305440616354152450)
    Amb = guild.get_role(549298356502134787)

    @commands.command(name="channelhide", aliases=["chide"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def viewNo(self, ctx):
        """Turn View Channel permissions OFF for Madridistras!, Ambassadors"""
        await ctx.channel.set_permissions(Madrid, read_messages=False)
        await ctx.channel.set_permissions(Amb, read_messages=False)
        await ctx.message.delete()

    @commands.command(name="channelshow", aliases=["cshow"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def viewYes(self, ctx):
        """Turn View Channel permissions ON for Madridistras!, Ambassadors"""
        await ctx.channel.set_permissions(Madrid, read_messages=True)
        await ctx.channel.set_permissions(Amb, read_messages=True)
        await ctx.message.delete()

    @commands.command(name="channelnotype", aliases=["cnotype"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def typeNo(self, ctx):
        """Turn Send Messages permissions OFF for Madridistras!, Ambassadors"""
        await ctx.channel.set_permissions(Madrid, send_messages=False)
        await ctx.channel.set_permissions(Amb, send_messages=False)
        await ctx.message.delete()

    @commands.command(name="channeltype", aliases=["ctype"])
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def typeYes(self, ctx):
        """Turn Send Messages permissions ON for Madridistras!, Ambassadors"""
        await ctx.channel.set_permissions(Madrid, send_messages=True)
        await ctx.channel.set_permissions(Amb, send_messages=True)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(ChannelPerms(bot))
