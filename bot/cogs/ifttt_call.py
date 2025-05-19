import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import aiohttp

class IFTTTCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="call")
    async def call(self, ctx, *, message):
        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) <= max_length:
            report = {
                "value1": f"New message. {message}",
                "value2": f". Sent by {ctx.author.name} on the server {ctx.guild.name}."
            }
            async with aiohttp.ClientSession() as session:
                await session.post(
                    f"https://maker.ifttt.com/trigger/{self.bot.config['eventName']}/with/key/{self.bot.config['IFTTTkey']}",
                    data=report
                )
            await ctx.send("**Data posted! Calling the bot owner now :telephone_receiver:**")
        else:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")

def setup(bot):
    bot.add_cog(IFTTTCallCog(bot))
