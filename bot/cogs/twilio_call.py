from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
from twilio.rest import Client

class TwilioCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.twilio_sid = cfg.get("twilio_account_sid")
        self.twilio_token = cfg.get("twilio_auth_token")
        self.from_number = cfg.get("twilio_from_number")
        self.to_number = cfg.get("twilio_to_number")
        self.enabled = all([self.twilio_sid, self.twilio_token, self.from_number, self.to_number])

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="twilio_call")
    async def twilio_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("Twilio integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        client = Client(self.twilio_sid, self.twilio_token)
        try:
            call = client.calls.create(
                twiml=f'<Response><Say>{message}</Say></Response>',
                to=self.to_number,
                from_=self.from_number
            )
            await ctx.send(f"**Twilio call initiated! Call SID: {call.sid} :telephone_receiver:**")
        except Exception as e:
            await ctx.send(f"Failed to initiate Twilio call: {e}")

def setup(bot):
    bot.add_cog(TwilioCallCog(bot))
