import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class WelcomeLater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="welcome", aliases=["w"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def welcome(self, ctx):
        member = ctx.guild.get_member(ctx.thread.recipient.id)
        channel = ctx.guild.get_channel(733193999942287441)
        
        await channel.send('Welcome to the squad, ' + str(member.mention) + '!')
               
def setup(bot):
    bot.add_cog(WelcomeLater(bot))
