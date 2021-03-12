import discord
from discord.ext import commands

class CasinoInvite(commands.Cog):
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        try:
            guild = self.bot.get_guild(173554823633829888)
            member = guild.get_member(after.id)
            juvC = guild.get_role(603767565130399784)
            socios = guild.get_role(541375823395946522)
            if juvC not in before.roles and juvC in after.roles and socios not in after.roles:
                print(f"{member.name} test dm message send")
                await member.send('test dm message')
        except AttributeError as e:
            print(e)
               
def setup(bot):
    bot.add_cog(CasinoInvite(bot))
