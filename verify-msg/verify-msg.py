from discord.ext import commands
import discord

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
    guild = self.bot.get_guild(173554823633829888)
    unverified = guild.get_role(1271869103564394611)
      if unverified in creator.roles:
        await thread.channel.send(str(";verify"))
      else:
        return
        
async def setup(bot):
    await bot.add_cog(Verify(bot))
