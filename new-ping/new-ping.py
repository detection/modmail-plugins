from discord.ext import commands
import discord
import asyncio

class NewPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v2.0.0')

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        category_id = 649463797949399050

        # Create a clickable ping for new member
        if channel.category.id == category_id:
            await asyncio.sleep(5)
            messages = await channel.history().flatten()
            first_msg = messages[0]
            print('First message: ', first_msg)
            newChannel = self.bot.get_channel(channel.id)
            userID = newChannel.topic.split(': ')[1]
            print('userID:', userID)

            ctx = await self.bot.get_context(first_msg)

            member = self.bot.get_user(int(userID))
            print("Member: ", member)
            
            thr = await self.bot.threads.find_or_create(member)
            ctx.thread = thr
        else:
            print('Wrong category')
            print(channel.category.name)

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.send(message)

def setup(bot):
    bot.add_cog(NewPing(bot))
