from discord.ext import commands
import discord

class NoEmotes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(self, payload):
    if payload.channel_id == 305599363219062785:
      await payload.message_id.clear_reactions()
    else:
      pass

def setup(bot):
  bot.add_cog(NoEmotes(bot))
