from discord.ext import commands
import discord
import asyncio

class NewPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v2.0.0')

    @commands.Cog.listener()
    async def on_guild_channel_create(self, channel):
        rma_id = 649463797949399050
        rmj_id = 719324997461606455

        if channel.category.id == rma_id or rmj_id:
            await asyncio.sleep(1)
            messages = await channel.history().flatten()
            newChannel = self.bot.get_channel(channel.id)
            userID = newChannel.topic.split(': ')[1]
            print('userID:', userID)

            member = self.bot.get_user(int(userID))
            print("Member: ", member)

            await newChannel.send(str(member.mention))
        else:
            print('Wrong category')
            print(channel.category.name)

def setup(bot):
    bot.add_cog(NewPing(bot))
