from buttplug.client import ButtplugClient
import discord
from discord.ext import commands

import lewd_manager as lm

class LewdCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.buttplug_client = ButtplugClient("Lewd Bot")

    @commands.command()
    async def ping(self, ctx: commands.Context):
        await ctx.send("pong!")
        
    @commands.command()
    async def test(self, ctx: commands.Context):
        pass