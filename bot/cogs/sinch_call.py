from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from sinch import SinchClient

class SinchCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.key_id = cfg.get("sinch_key_id")
        self.key_secret = cfg.get("sinch_key_secret")
        self.from_number = cfg.get("sinch_from_number")
        self.to_number = cfg.get("sinch_to_number")
        self.enabled = all([self.key_id, self.key_secret, self.from_number, self.to_number])
        if self.enabled:
            self.client = SinchClient(key_id=self.key_id, key_secret=self.key_secret)
        else:
            self.client = None

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="sinch_call")
    async def sinch_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("Sinch integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        try:
            response = self.client.voice.callouts.tts(
                to=self.to_number,
                from_=self.from_number,
                text=message
            )
            call_id = response.get("callId", "unknown")
            await ctx.send(f"**Sinch call initiated! Call ID: {call_id} :telephone_receiver:**")
        except Exception as e:
            await ctx.send(f"Failed to initiate Sinch call: {e}")

def setup(bot):
    bot.add_cog(SinchCallCog(bot))
