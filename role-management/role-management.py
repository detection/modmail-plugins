import discord
from discord.ext import commands

class RoleManage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        guild = self.bot.get_guild(173554823633829888)
        user = guild.get_member(after.id)

        color_roles = [753329075694600393, 859881708673564713, 753416121943720037, 753416717450870916, 753417031243792484, 753417173271183454, 753417480571060264, 753417665996914738, 753417999796535356, 753418176053903431, 859881464064376832, 1128447942127255715, 1128442780855828553, 1128442696663584828, 1128442836958851072, 753418170722680852, 753418170722680852] # list of ids
        player_roles = [1130530731295260763, 1130530785678590083, 1130530268076318720, 1130157887797342259, 1130530758994432091, 1130157667541860432, 1130530809246384259, 1130530663406260325, 1130530454915797002, 1130158069993721987, 1130157802195791912, 1130517417211207690, 1130517513478877314, 1130521247453810798, 1130517467526078557, 1130521375841452102, 1271877076655538258, 1271880442718589020, 1271876919129931856, 1271881292690231308, 1271870588939538452, 1130530731295260763, 1271885473232715786, 1271887731072569374, 1271889128400879627, 1271889792820580445, 1271889885824946196, 1271890005718991028, 1399078999468015796, 1399075390760161382, 1399450779978301511, 1399090429634543696, 1399070429389520967, 1398870205085782026, 1398919822569373756] # list of ids

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

async def setup(bot):
    await bot.add_cog(RoleManage(bot))
