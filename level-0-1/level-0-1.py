import discord
from discord.ext import commands

class Level01(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @bot.event
    async def on_member_update(before, after):
        nego = ctx.guild.get_role(732405243299495968)
        ns = ctx.guild.get_role(603767376852287502)
        if after.roles === ns:
          await user.remove_roles(nego)
      else
        return
               
def setup(bot):
    bot.add_cog(Level01(bot))
