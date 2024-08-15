import discord
from discord.ext import commands

class MadridDM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(173554823633829888)
        member = guild.get_member(after.id)
        premadrid = guild.get_role(1271869103564394611)
        madrid = guild.get_role(305440616354152450)
        
        if premadrid not in before.roles and premadrid in after.roles and madrid not in after.roles:
            print(f"{member.name} test dm message send")
            await member.send("""Hello, and welcome to the Real Madrid Discord Server! The majority of our server is Madridista-exclusive, if you could please answer the following questions to complete your joining process:

- How long have you been supporting the club, and what's your favorite memory?
- Do you support any other clubs? If yes, whom and why?
- What are your thoughts on Real Madrid Femenino?

Please share your reddit username if you came from /r/realmadrid. Thank you! <:madridista:350639920504766476>""")
        
        elif premadrid in after.roles and madrid in after.roles:
            await after.remove_roles(premadrid)
        
        else:
            return
               
async def setup(bot):
    await bot.add_cog(MadridDM(bot))
