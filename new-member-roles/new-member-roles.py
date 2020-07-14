import discord
import typing
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class NewMemberRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="approve", aliases=["app"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def approve(self, ctx):
        member = ctx.thread.recipient.id
        pend = ctx.guild.get_role(324658636574162945)
        nego = ctx.guild.get_role(732405243299495968)
        madrid = ctx.guild.get_role(305440616354152450)
        await member.add_roles(nego, madrid)
        await member.remove_roles(pend)
        
        config = await self.db.find_one({"_id": "config"})

        await ctx.send("{member} has been successfully approved!")

def setup(bot):
    bot.add_cog(NewMemberRoles(bot))
