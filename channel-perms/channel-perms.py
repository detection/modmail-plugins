import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class ChannelPerms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="channelhide", aliases=["chide"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def viewNo(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        role = guild.get_role(821435409397055528) #Madridistras! 
        await ctx.channel.set_permissions(ctx.guild.role, read_messages=False)
        
    @commands.command(name="channelshow", aliases=["cshow"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def viewYes(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        role = guild.get_role(821435409397055528) #Madridistras!
        await ctx.channel.set_permissions(ctx.guild.role, read_messages=True)
        
    @commands.command(name="channelnotype", aliases=["cnotype"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def typeNo(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        role = guild.get_role(821435409397055528) #Madridistras!
        await ctx.channel.set_permissions(ctx.guild.role, send_messages=False)
        
    @commands.command(name="channeltype", aliases=["ctype"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def typeYes(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        role = guild.get_role(821435409397055528) #Madridistras! 305440616354152450
        await ctx.channel.set_permissions(ctx.guild.role, send_messages=True)
               
def setup(bot):
    bot.add_cog(ChannelPerms(bot))
