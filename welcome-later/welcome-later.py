import json

import discord
from box import Box
from discord.ext import commands

from .models import apply_vars, SafeString


class WelcomeLater(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = bot.plugin_db.get_partition(self)

    def apply_vars_dict(self, member, message, invite):
        for k, v in message.items():
            if isinstance(v, dict):
                message[k] = self.apply_vars_dict(member, v, invite)
            elif isinstance(v, str):
                message[k] = apply_vars(self, member, v, invite)
            elif isinstance(v, list):
                message[k] = [self.apply_vars_dict(member, _v, invite) for _v in v]
            if k == 'timestamp':
                message[k] = v[:-1]
        return message

    def format_message(self, member, message, invite):
        try:
            message = json.loads(message)
        except json.JSONDecodeError:
            # message is not embed
            message = apply_vars(self, member, message, invite)
            message = {'content': message}
        else:
            # message is embed
            message = self.apply_vars_dict(member, message, invite)

            if any(i in message for i in ('embed', 'content')):
                message['embed'] = discord.Embed.from_dict(message['embed'])
            else:
                message = None
        return message

    @commands.has_permissions(manage_guild=True)
    @commands.command()
    async def welcome(self, ctx, channel: discord.TextChannel, *, message):
        """Sets up welcome command. Check [here](https://github.com/fourjr/modmail-plugins/blob/master/welcomer/README.md)
        for complex usage.
        """
        # Example usage: `welcome #general Hello {member.name}`
        # """
        if message.startswith('https://') or message.startswith('http://'):
            # message is a URL
            if message.startswith('https://hasteb.in/'):
                message = 'https://hasteb.in/raw/' + message.split('/')[-1]

            async with self.bot.session.get(message) as resp:
                message = await resp.text()

        formatted_message = self.format_message(ctx.author, message, SafeString('{invite}'))
        if formatted_message:
            await channel.send(**formatted_message)
            await self.db.find_one_and_update(
                {'_id': 'config'},
                {'$set': {'welcome': {'channel': str(channel.id), 'message': message}}},
                upsert=True
            )
            await ctx.send(f'Message sent to {channel.mention} for testing.\nNote: invites cannot be rendered in test message')
        else:
            await ctx.send('Invalid welcome message syntax.')

    @commands.Cog.listener()
    async def on_member_update(before, after):
        if after.roles = ctx.guild.get_role(305440616354152450)
        config = (await self.db.find_one({'_id': 'config'}))['welcome']
        if config:
            channel = member.guild.get_channel(int(config['channel']))
            if channel:
                message = self.format_message(member, config['message'], invite)
                if message:
                    await channel.send(**message)
                else:
                    await channel.send('Invalid welcome message')
            else:
                print('WelcomeLater plugin not found: {getattr(channel, "id", None}')


def setup(bot):
    bot.add_cog(WelcomeLater(bot))
