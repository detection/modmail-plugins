import discord
from discord.ext import commands
import random

from core import checks
from core.models import PermissionLevel

class WelcomeLater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="welcome", aliases=["w"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def welcome(self, ctx):
        """Announce a new member in welcome channel."""
        member = ctx.guild.get_member(ctx.thread.recipient.id)
        channel = ctx.guild.get_channel(733193999942287441)

        welcome_messages = [
            f"{member.mention} just made their debut for the Real Madrid Discord Server—what a signing! ⚽️",
            f"Everyone give {member.mention} a warm Bernabéu welcome! 🏟️",
            f"{member.mention} just transferred in—contract signed, give 'em a welcome! 👋",
            f"Fresh boots on the pitch! Say hi to {member.mention}, our newest galáctico. 💫",
            f"{member.mention} just got called up to the first team. Let's give 'em a champion's welcome! 🏆"
            f"{member.mention} just stepped into the Santiago Bernabéu—welcome to the home of legends! 👑"
        ]

        await channel.send(random.choice(welcome_messages))

async def setup(bot):
    await bot.add_cog(WelcomeLater(bot))
