from discord.ext import commands
import discord

class NewPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        thread_channel = self.bot.get_channel(thread.channel.id)
        member = self.bot.guild.get_member(thread.recipient.id)
            
        await thread_channel.send(str(member.mention))

def setup(bot):
    bot.add_cog(NewPing(bot))
