from discord.ext import commands
import discord

class NewPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
            
        await thread.channel.send(str(thread.recipient.mention))

def setup(bot):
    bot.add_cog(NewPing(bot))
