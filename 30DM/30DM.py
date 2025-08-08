import discord
from discord.ext import commands
import asyncio

class ThirtyMinuteDM(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if member.guild.id != 173554823633829888:
            return

        await asyncio.sleep(30)

        if member not in member.guild.members:
            return

        visitor = member.guild.get_role(324658636574162945)
        if visitor in member.roles:
            try:
                view = VerificationButtons()
                await member.send(
                    "Welcome to Real Madrid Discord Server! We noticed you haven’t completed verification yet. "
                    "Please choose a button below, or just reply here to contact server staff if you have any questions. Thanks!",
                    view=view
                )
                print(f"DM with buttons sent to {member.name}")
            except discord.Forbidden:
                print(f"Could not DM {member.name} (DMs closed).")

class VerificationButtons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="I'm a Madridista!", style=discord.ButtonStyle.primary, emoji="⚪")
    async def madridista_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Hello! If you could please answer the following questions, we'll proceed with your verification process:\n\n"
            "- Who/what inspired you to be a Madridista?\n"
            "- What is your most and least favorite aspect of the club?\n"
            "- What are your thoughts on Real Madrid Femenino (Real Madrid Women's Team)?\n\n"
            "Finally, do you support any other club?\n\n"
            "Thank you! <:madridista:350639920504766476>",
            ephemeral=False
        )

    @discord.ui.button(label="Just visiting", style=discord.ButtonStyle.secondary, emoji="👋")
    async def visitor_button(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message(
            "Thanks for joining! Please feel free to explore the Visitors section, more access unlocks as you level up.",
            ephemeral=False
        )

async def setup(bot):
    await bot.add_cog(ThirtyMinuteDM(bot))
