from discord.ext import commands
import discord

class Verify(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_thread_ready(self, thread, creator, category, initial_message):
        guild = self.bot.get_guild(173554823633829888)
        member = await guild.fetch_member(thread.recipient.id)
        unverified = guild.get_role(1271869103564394611)
        ctx = await self.bot.get_context(initial_message)
        thr = await self.bot.threads.find_or_create(member)
        ctx.thread = thr
        
        if unverified in member.roles:
            await ctx.invoke(self.bot.get_command('verify'))
            # await thread.reply("Hello! Please verify your account through the <@703886990948565003> prompt sent to your DMs.\nIf the link expired by the time you attempt verification, you can send yourself a new one by sending the `/verify` command in any channel within the server.")
        else:
            return
            
async def setup(bot):
    await bot.add_cog(Verify(bot))
