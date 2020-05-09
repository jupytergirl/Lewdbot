# main.py

import discord
from discord.ext import commands
import buttplug

from lewd_cog import LewdCog
import secret

description = 'lewd bot'

bot = commands.Bot(command_prefix='$', description=description)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('--------')

bot.add_cog(LewdCog)

bot.run(secret.token)
