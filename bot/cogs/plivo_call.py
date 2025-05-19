from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import plivo

class PlivoCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.auth_id = cfg.get("plivo_auth_id")
        self.auth_token = cfg.get("plivo_auth_token")
        self.from_number = cfg.get("plivo_from_number")
        self.to_number = cfg.get("plivo_to_number")
        self.enabled = all([self.auth_id, self.auth_token, self.from_number, self.to_number])
        if self.enabled:
            self.client = plivo.RestClient(self.auth_id, self.auth_token)
        else:
            self.client = None

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="plivo_call")
    async def plivo_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("Plivo integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        answer_url = f"https://s3.amazonaws.com/plivocloud/PlivoTTS.xml?text={message}"
        try:
            response = self.client.calls.create(
                from_=self.from_number,
                to=self.to_number,
                answer_url=answer_url,
                answer_method='GET'
            )
            call_id = getattr(response, 'request_uuid', 'unknown')
            await ctx.send(f"**Plivo call initiated! Call UUID: {call_id} :telephone_receiver:**")
        except Exception as e:
            await ctx.send(f"Failed to initiate Plivo call: {e}")

def setup(bot):
    bot.add_cog(PlivoCallCog(bot))
