import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class ChannelPerms(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    #Madridistras! 305440616354152450
    #Tester 821435409397055528

    @commands.command(name="channelhide", aliases=["chide"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def viewNo(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        await ctx.channel.set_permissions(ctx.guild.get_role(305440616354152450), read_messages=False)
        await ctx.message.delete()
        
    @commands.command(name="channelshow", aliases=["cshow"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def viewYes(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        await ctx.channel.set_permissions(ctx.guild.get_role(305440616354152450), read_messages=True)
        await ctx.message.delete()
        
    @commands.command(name="channelnotype", aliases=["cnotype"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def typeNo(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        await ctx.channel.set_permissions(ctx.guild.get_role(305440616354152450), send_messages=False)
        await ctx.message.delete()
        
    @commands.command(name="channeltype", aliases=["ctype"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def typeYes(self, ctx):
        guild = self.bot.get_guild(173554823633829888)
        await ctx.channel.set_permissions(ctx.guild.get_role(305440616354152450), send_messages=True)
        await ctx.message.delete()
               
def setup(bot):
    bot.add_cog(ChannelPerms(bot))
