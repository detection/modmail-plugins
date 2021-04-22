from discord.ext import commands
import discord
import asyncio

class RedditCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v1.0.0')

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):

        print(initial_message)
        new_channel = self.bot.get_channel(thread.channel.id)
        print(new_channel)
        first_message = initial_message
        print(first_message)
        first_line = first_message.splitlines()[0]
        skip_words = ['dont have', 'don\'t', 'dont use', 'no reddit', 'anonymous']
        bad_chars = [' ', 'u/', "/u/", "1.", "1)", "#1"]
        dash_first = ['-']

        for i in bad_chars:
          first_line = first_line.replace(i, '')

        for i in dash_first:
          if first_line[0] == "-":
             first_line = first_line.replace(i, '', 1)

        await new_channel.send('https://redditmetis.com/user/' + str(first_line))
            
def setup(bot):
    bot.add_cog(RedditCheck(bot))
