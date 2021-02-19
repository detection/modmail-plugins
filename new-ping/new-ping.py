from discord.ext import commands
import discord
import asyncio

class NewPing(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print('v2.0.0')

    @commands.command()
    async def on_guild_channel_create(self, channel):
        category_id = 649463797949399050
        member = ctx.guild.get_member(ctx.thread.recipient.id)

        if channel.category.id == category_id:
            await asyncio.sleep(5)
            messages = await channel.history().flatten()

        else:
            print('Wrong category')
            print(channel.category.name)

    async def say(self, ctx, *, message):
        await ctx.send(str(member.mention))

def setup(bot):
    bot.add_cog(NewPing(bot))
