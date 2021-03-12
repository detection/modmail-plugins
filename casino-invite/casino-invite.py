import discord
from discord.ext import commands

class CasinoInvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(173554823633829888)
        member = guild.get_member(after.id)
        juvC = guild.get_role(603767565130399784)
        socios = guild.get_role(541375823395946522)
        self_roles = guild.get_channel(800176964559306814)
        if juvC not in before.roles and juvC in after.roles and socios not in after.roles:
            print(f"{member.name} test dm message send")
            await member.send("""Congratulations, you've reached Level 20 in the Real Madrid Discord server! Please accept this invitation to our exclusive Casino Royale, where we gamble our very own currency, the Flocoin.\nHead to""" + self_roles + """and tap the <:flocoin:541110660545773618> to enter. Good luck!""")
        else:
            return
               
def setup(bot):
    bot.add_cog(CasinoInvite(bot))
