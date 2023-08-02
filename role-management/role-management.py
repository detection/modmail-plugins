import discord
from discord.ext import commands

class RoleManage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(173554823633829888)
        user = guild.get_member(after.id)

        color_roles = [753329075694600393, 859881708673564713, 753416121943720037, 753416717450870916, 753417031243792484, 753417173271183454, 753417480571060264, 753417665996914738, 753417999796535356, 753417999796535356, 753418176053903431, 859881464064376832, 1128447942127255715, 1128442780855828553] # list of ids
        player_roles = [1130530731295260763, 1130530785678590083, 1130530268076318720, 1130157887797342259, 1130530758994432091, 1130157667541860432, 1130530809246384259, 1130530663406260325, 1130530454915797002, 1130158069993721987, 1130157802195791912, 1130517417211207690, 1130517513478877314, 1130521247453810798, 1130517467526078557, 1130521375841452102] # list of ids

        added_roles = [] # roles that are in after.roles but not before.roles

        # Actually find the newly added roles
        for role in after.roles:
          if role not in before.roles:
            added_roles.append(role.id)

        for role_id in added_roles:
          if role_id in color_roles:
            # There is a new color role added
            color_roles.remove(role_id) # removes the newly added role id from the full list

            for color_role_id in color_roles:
              await user.remove_roles(guild.get_role(color_role_id))

            return

        for role_id in added_roles:
          if role_id in player_roles:
            # There is a new color role added
            player_roles.remove(role_id) # removes the newly added role id from the full list

            for player_role_id in player_roles:
              await user.remove_roles(guild.get_role(player_role_id))

            return

        training = guild.get_role(732405243299495968)
        ns = guild.get_role(603767376852287502)
        juvC = guild.get_role(603767565130399784)
        socios = guild.get_role(541375823395946522)

        if juvC not in before.roles and juvC in after.roles and socios not in after.roles:
            await user.send("""**Congratulations!** You've reached Level 20 in the Real Madrid Discord Server! Please accept this invitation to our exclusive *Casino Royale*, where we gamble our very own currency, the Flocoin.\n\nHead to <#800176964559306814> and tap the <:flocoin:541110660545773618> to enter. Good luck!""")
            await user.remove_roles(training)
        elif juvC not in before.roles and juvC in after.roles:
            await user.remove_roles(training)
        else:
            return

async def setup(bot):
    await bot.add_cog(RoleManage(bot))
