import discord
from discord.ext import commands
import asyncio

class 30DM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Only for RMDS
        if member.guild.id != 173554823633829888:
            return
        
        # Wait 30 minutes
        await asyncio.sleep(1800)

        # Check if member still exists in RMDS
        if member not in member.guild.members:
            return

        # Check if Visitor
        visitor = member.guild.get_role(324658636574162945)
        if visitor in member.roles:
            try:
                await member.send(
                    "**Hey there!** Thanks for joining the Real Madrid Discord! "
                    "Check out our exclusive channels and get involved in the community! ⚽"
                )
                print(f"DM sent to {member.name}")
            except discord.Forbidden:
                print(f"Could not DM {member.name} (DMs closed).")

async def setup(bot):
    await bot.add_cog(30DM(bot))
