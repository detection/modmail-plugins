import discord
from discord.ext import commands

class Level01(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = bot.get_guild(173554823633829888)
        nego = guild.get_role(732405243299495968)
        ns = guild.get_role(603767376852287502)
        user = bot.get_member(after.id)
        if ns not in before.roles and ns in after.roles:
            await user.remove_roles(nego)
        else:
            return
               
def setup(bot):
    bot.add_cog(Level01(bot))
