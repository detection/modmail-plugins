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
        member = ctx.guild.get_member(channel.thread.recipient.id)
        newthread = ctx.guild.get_channel(channel.thread.channel.id)

        if channel.category.id == category_id:
            await asyncio.sleep(5)
            await newthread.send(str(member.mention))

        else:
            print('Wrong category')
            print(channel.category.name)

def setup(bot):
    bot.add_cog(NewPing(bot))
