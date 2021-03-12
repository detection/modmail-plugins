import discord
from discord.ext import commands

from core import checks
from core.models import PermissionLevel

class CasinoInvite(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["ci"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def casino_invite(self, ctx, *, message):
        """Set a message to DM a user after they reach Level 20."""
        if message.startswith("https://") or message.startswith("http://"):
            # message is a URL
            if message.startswith("https://hasteb.in/"):
                message = "https://hasteb.in/raw/" + message.split("/")[-1]

            async with self.bot.session.get(message) as resp:
                message = await resp.text()

        await self.db.find_one_and_update(
            {"_id": "ci-dm-config"},
            {"$set": {"ci-dm-message": {"ci-message": message}}},
            upsert=True,
        )

        await ctx.send("Successfully set the message.")
    
    @commands.Cog.listener()
    async def on_member_update(self, before, after):
    	config = await self.db.find_one({"_id": "ci-dm-config"})
        guild = self.bot.get_guild(173554823633829888)
        user = guild.get_member(after.id)
        juvC = guild.get_role(603767565130399784)
        socios = guild.get_role(541375823395946522)
        if juvC not in before.roles and juvC in after.roles and socios not in after.roles:
            message = config["ci-dm-message"]["ci-message"]
            await member.send(message.replace("{user}", str(member))) 
        else:
            return
               
def setup(bot):
    bot.add_cog(CasinoInvite(bot))