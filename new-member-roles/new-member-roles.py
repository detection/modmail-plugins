from discord.ext import commands

class NewMemberRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
      pend = discord.utils.get(memberafter.server.roles, name="Pending")
      nego = discord.utils.get(memberafter.server.roles, name="Negotiating")
      madrid = discord.utils.get(memberafter.server.roles, name="Madridistas!")

      if "Minecraft" in totestafter:     
        await client.add_roles(memberafter, mcrole, playing)
      elif "Minecraft" in totestbefore:
        await client.remove_roles(memberafter, mcrole, playing)

    @commands.command(name="newmemberroles", aliases=["nmr"], invoke_without_command=True)
    @checks.has_permissions(PermissionLevel.ADMINISTRATOR)

def setup(bot):
    bot.add_cog(NewMemberRolesPlugin(bot))
