from discord.ext import commands
import discord

class NoEmotes(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_raw_reaction_add(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    if channel == 305599363219062785:
      await message.clear_reactions()
    else:
      pass

def setup(bot):
  bot.add_cog(NoEmotes(bot))
