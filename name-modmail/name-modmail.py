import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class NameModmail(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="newname", aliases=["newn"])
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)
    async def rename(ctx, name):
    await ctx.user.edit(username=Papa Flo)
               
def setup(bot):
    bot.add_cog(NameModmail(bot))
