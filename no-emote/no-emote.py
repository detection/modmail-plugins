from discord.ext import commands
import discord

class NoEmotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        guild = self.bot.get_guild(payload.guild_id)
        channel = self.bot.get_channel(payload.channel_id)
        member = guild.get_member(payload.user_id)
        vp = guild.get_role(812426821010194463)
        message = channel.get_partial_message(payload.message_id)
        if channel.id == 907310047548309514 and vp in member.roles:
            await message.clear_reactions()
        else:
            pass

def setup(bot):
  bot.add_cog(NoEmotes(bot))
