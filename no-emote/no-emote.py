from discord.ext import commands
import discord

class NoEmotes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(reaction, user):
    if reaction.message.channel.id == 305599363219062785:
      await reaction.remove(user)
    else:
      pass

def setup(bot):
  bot.add_cog(NoEmotes(bot))
