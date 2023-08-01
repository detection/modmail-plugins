import discord
from discord.ext import commands

class ReportReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(reaction, user):
        if reaction.emoji == '🆘':
            
        else:
            return
               
async def setup(bot):
    await bot.add_cog(ReportReact(bot))
