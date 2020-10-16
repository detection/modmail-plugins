import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel


class KickPending(commands.Cog):
    """
    Kick all users with Pending role
    """

    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    @commands.command(name="thepurge", aliases=["kickpend"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def kick(self, ctx):
        role = ctx.guild.get_role(324658636574162945)
        for x in role.members:
            await x.kick(reason="Inactivity")
            await ctx.send("Kicked all members with role Pending")
        
        config = await self.db.find_one({"_id": "config"})

        if config is None:
            return await ctx.send("There's no configured log channel.")
        else:
            channel = ctx.guild.get_channel(int(config["channel"]))

        if channel is None:
            await ctx.send("There is no configured log channel.")
            return

        try:
            for member in members:
                await member.kick(reason=f"{reason if reason else None}")
                embed = discord.Embed(
                    color=discord.Color.red(),
                    title=f"{member} was kicked!",
                    timestamp=datetime.datetime.utcnow(),
                )

                embed.add_field(
                    name="Moderator", value=f"{ctx.author}", inline=False,
                )

                if reason is not None:
                    embed.add_field(name="Reason", value=reason, inline=False)

                    await ctx.send(f"🦶 | {member} is kicked!")
                    await channel.send(embed=embed)
        except:
            return

def setup(bot):
    bot.add_cog(KickPending(bot))
