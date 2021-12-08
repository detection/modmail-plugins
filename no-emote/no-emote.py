from discord.ext import commands
import discord

class NoEmotes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_reaction_add(reaction, user):
    if reaction.message.channel.id == 907310047548309514:
      await reaction.remove(user)
    else:
      pass

def setup(bot):
  bot.add_cog(NoEmotes(bot))
