from discord.ext import commands

class NewMemberRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="newmemberroles", aliases=["approve"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def approve(self, ctx):
        pend = discord.utils.get(memberafter.server.roles, name="Pending")
        nego = discord.utils.get(memberafter.server.roles, name="Negotiating")
        madrid = discord.utils.get(memberafter.server.roles, name="Madridistas!")
        await client.add_roles(nego, madrid)
        await client.remove_roles(pend)
        
        config = await self.db.find_one({"_id": "config"})

        await ctx.send("Successfully approved.")

def setup(bot):
    bot.add_cog(NewMemberRolesPlugin(bot))
