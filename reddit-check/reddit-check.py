from discord.ext import commands
import discord

class RedditCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v1.0.0')

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):

        thread_channel = self.bot.get_channel(thread.channel.id)
        member = self.bot.guild.get_member(thread.recipient.id)
        pending = self.bot.guild.get_role(324658636574162945)
        first_line = initial_message.content.splitlines()[0]
        skip_words = ['dont have', 'don\'t', 'dont use', 'no reddit', 'anonymous']
        bad_chars = [' ', 'u/', "/u/", "1.", "1)", "#1"]
        dash_first = ['-']

        if pending in member.roles:
            if any(i in first_line for i in skip_words) == False:
                print(skip_all)
                if "," in first_line[0:20]:
                    before_comma = first_line.partition(',')
                    first_line = before_comma[0]

                for i in bad_chars:
                    first_line = first_line.replace(i, '')

                for i in dash_first:
                    if first_line[0] == "-":
                        first_line = first_line.replace(i, '', 1)

            await thread_channel.send('https://redditmetis.com/user/' + str(first_line))
            
        else:
            pass
            
def setup(bot):
    bot.add_cog(RedditCheck(bot))
