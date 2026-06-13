import discord
from discord.ext import commands
import asyncio

class ReportReact(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.bot:
            return

        if reaction.emoji != '🆘':
            return

        reported_message = reaction.message

        thread = await self.bot.threads.create(user, creator=self.bot.user)

        await asyncio.sleep(2)

        genesis_msg = await thread.get_genesis_message()
        ctx = await self.bot.get_context(genesis_msg)

        message_content = reported_message.content or "*No text content. Message may contain attachment(s) only.*"
        quoted_message = "\n".join([f"> {line}" for line in message_content.splitlines()])

        embed = discord.Embed(
            title="Incident Report",
            description=f"**Reported Message:**\n\n{quoted_message}",
            color=discord.Color.red(),
            timestamp=reported_message.created_at
        )

        embed.add_field(
            name="Message author",
            value=f"{reported_message.author.mention} (`{reported_message.author.id}`)",
            inline=False
        )

        embed.add_field(
            name="Channel",
            value=reported_message.channel.mention,
            inline=False
        )

        embed.add_field(
            name="Jump link",
            value=f"[Go to message]({reported_message.jump_url})",
            inline=False
        )

        embed.add_field(
            name="Reported by",
            value=f"{user.mention} (`{user.id}`)",
            inline=False
        )

        if reported_message.attachments:
            attachment_links = []

            for attachment in reported_message.attachments:
                attachment_links.append(f"[{attachment.filename}]({attachment.url})")

                if attachment.content_type and attachment.content_type.startswith("image/"):
                    embed.set_image(url=attachment.url)

            embed.add_field(
                name="Attachments",
                value="\n".join(attachment_links)[:1024],
                inline=False
            )

        if reported_message.embeds:
            embed.add_field(
                name="Embeds",
                value=f"{len(reported_message.embeds)} embed(s) attached to original message.",
                inline=False
            )

        await ctx.send(embed=embed)

        ctx.thread = thread
        await ctx.invoke(
            self.bot.get_command('areply'),
            msg="Thank you for your report, please reply with any additional information you think we need to proceed."
        )

        try:
            await reaction.clear()
        except discord.Forbidden:
            pass

async def setup(bot):
    await bot.add_cog(ReportReact(bot))
