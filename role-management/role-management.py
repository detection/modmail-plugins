import discord
from discord.ext import commands

class RoleManage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(173554823633829888)
        user = guild.get_member(after.id)
        nego = guild.get_role(732405243299495968)
        ns = guild.get_role(603767376852287502)
        red = guild.get_role(753329075694600393)
        orange = guild.get_role(753331480897388726)
        yellow = guild.get_role(753416121943720037)
        green = guild.get_role(753416717450870916)
        lime = guild.get_role(753417031243792484)
        seafoam = guild.get_role(753417173271183454)
        aqua = guild.get_role(753417480571060264)
        blue = guild.get_role(753417665996914738)
        lav = guild.get_role(753417999796535356)
        violet = guild.get_role(753418170722680852)
        indigo = guild.get_role(753418176053903431)
        if ns not in before.roles and ns in after.roles:
            await user.remove_roles(nego)
        elif red not in before.roles and red in after.roles:
            await user.remove_roles(orange, yellow, green, lime, seafoam, aqua, blue, lav, violet, indigo)
        else:
            return           
def setup(bot):
    bot.add_cog(RoleManage(bot))
