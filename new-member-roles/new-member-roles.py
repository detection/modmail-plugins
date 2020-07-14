from discord.ext import commands

class NewMemberRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="approve", aliases=["app"])
    @checks.has_permissions(PermissionLevel.MODERATOR)
    async def approve(self, ctx):
        member = """USER ID FROM MODMAIL CHANNEL"""
        pend = discord.utils.get(ctx.server.roles, name="Pending")
        nego = discord.utils.get(ctx.server.roles, name="Negotiating")
        madrid = discord.utils.get(ctx.server.roles, name="Madridistas!")
        await client.add_roles(member, nego, madrid)
        await client.remove_roles(member, pend)
        
        config = await self.db.find_one({"_id": "config"})

        await ctx.send("{member} has been successfully approved!")

def setup(bot):
    bot.add_cog(NewMemberRolesPlugin(bot))
