from discord.ext import commands
import discord
import asyncio

class RedditCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v1.0.0')

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):

        thread_channel = self.bot.get_channel(thread.channel.id)
        first_message = initial_message.content
        first_line = first_message.splitlines()[0]
        skip_words = ['dont have', 'don\'t', 'dont use', 'no reddit', 'anonymous']
        bad_chars = [' ', 'u/', "/u/", "1.", "1)", "#1"]
        dash_first = ['-']

        if any(i in first_line for i in skip_words):
            skip_all = True
        else:
            skip_all = False

        if skip_all == False:
            if "," in first_line[0:20]:
                before_comma = first_line.partition(',')
                first_line = before_comma[0]

            for i in bad_chars:
                first_line = first_line.replace(i, '')

            for i in dash_first:
                if first_line[0] == "-":
                    first_line = first_line.replace(i, '', 1)

        await thread_channel.send('https://redditmetis.com/user/' + str(first_line))
            
def setup(bot):
    bot.add_cog(RedditCheck(bot))
