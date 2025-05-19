from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import vonage

class VonageCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.api_key = cfg.get("vonage_api_key")
        self.api_secret = cfg.get("vonage_api_secret")
        self.from_number = cfg.get("vonage_from_number")
        self.to_number = cfg.get("vonage_to_number")
        self.enabled = all([self.api_key, self.api_secret, self.from_number, self.to_number])
        if self.enabled:
            self.client = vonage.Client(key=self.api_key, secret=self.api_secret)
            self.voice = vonage.Voice(self.client)
        else:
            self.client = None
            self.voice = None

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="vonage_call")
    async def vonage_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("Vonage integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        ncco = [
            {
                "action": "talk",
                "voiceName": "Joanna",
                "text": message
            }
        ]
        try:
            response = self.voice.create_call({
                "to": [{"type": "phone", "number": self.to_number}],
                "from": {"type": "phone", "number": self.from_number},
                "ncco": ncco
            })
            call_id = response.get("uuid", "unknown")
            await ctx.send(f"**Vonage call initiated! Call UUID: {call_id} :telephone_receiver:**")
        except Exception as e:
            await ctx.send(f"Failed to initiate Vonage call: {e}")

def setup(bot):
    bot.add_cog(VonageCallCog(bot))
