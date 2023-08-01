import discord
from discord.ext import commands

import asyncio

class ReportReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '🆘':
            thread = await self.bot.threads.create(user, manual_trigger=False)
            await asyncio.sleep(2)
            genesis_msg = await thread.get_genesis_message()
            ctx = await self.bot.get_context(genesis_msg)
    
            thread.reply("Thank you for your report, please reply with any additional information you think we need to proceed.", True) # Second argument makes the message anon
            ctx.send(f"{user.mention} has reported an incident. Message link: {reaction.message.jump_url}") 
        else:
            return
               
async def setup(bot):
    await bot.add_cog(ReportReact(bot))
