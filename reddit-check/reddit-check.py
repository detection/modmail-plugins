from discord.ext import commands
import discord

class RedditCheck(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        member = self.bot.guild.get_member(thread.recipient.id)
        pending = self.bot.guild.get_role(324658636574162945)
        first_line = initial_message.content.splitlines()[0]
        skip_words = ["don't", "don’t", "don`t", "didn't", "didn’t", "didn`t", 'dont have', 'dont use', 'didnt have', 'didnt use', 'no reddit', 'anonymous', 'no have', 'dont reddit', 'didnt reddit', 'no tengo', 'not on', 'dont got']
        bad_chars = ['u/', '/', '1.', '1)', '#1', 'what is your', 'my reddit username is', 'reddit username is', 'reddit username', ':', '(', '?', ' ']
        dash_first = ['-']
        tag_hash = ['#']
        greeting = ['hello', 'hi', 'hola', 'none']

        if pending in member.roles:
            if any(i.lower() in first_line.lower() for i in skip_words) == False:
                if "," in first_line[0:30]:
                    before_comma = first_line.partition(',')
                    first_line = before_comma[0]

                if "." in first_line[3:30]:
                    before_period = first_line.partition('.')
                    first_line = before_period[0]

                if " -" in first_line[3:30]:
                    before_dash = first_line.partition(' -')
                    first_line = before_dash[0]

                for i in bad_chars:
                    first_line = first_line.lower()
                    first_line = first_line.replace(i, '')

                for i in dash_first:
                    if first_line[0] == '-':
                        first_line = first_line.replace(i, '', 1)

                if first_line.lower() in greeting: 
                    pass
                elif any(t.lower() in first_line.lower() for t in tag_hash): 
                    pass
                elif 3 < len(first_line) <= 20:
                    await thread.channel.send('https://redditmetis.com/user/' + str(first_line))
                    await thread.channel.send('https://www.reddit.com/user/' + str(first_line))

        else:
            pass

def setup(bot):
    bot.add_cog(RedditCheck(bot))
