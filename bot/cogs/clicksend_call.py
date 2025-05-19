from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import clicksend_client
from clicksend_client import VoiceApi, SmsMessage, VoiceMessage
from clicksend_client.rest import ApiException

class ClickSendCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.username = cfg.get("clicksend_username")
        self.api_key = cfg.get("clicksend_api_key")
        self.to_number = cfg.get("clicksend_to_number")
        self.voice = cfg.get("clicksend_voice", "female")
        self.language = cfg.get("clicksend_language", "en-us")
        self.enabled = all([self.username, self.api_key, self.to_number])
        if self.enabled:
            configuration = clicksend_client.Configuration()
            configuration.username = self.username
            configuration.password = self.api_key
            self.voice_api = VoiceApi(clicksend_client.ApiClient(configuration))
        else:
            self.voice_api = None

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="clicksend_call")
    async def clicksend_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("ClickSend integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        voice_message = VoiceMessage(
            to=self.to_number,
            body=message,
            voice=self.voice,
            lang=self.language
        )
        try:
            api_response = self.voice_api.voice_send_post(voice_message)
            await ctx.send("**ClickSend call initiated! :telephone_receiver:**")
        except ApiException as e:
            await ctx.send(f"Failed to initiate ClickSend call: {e}")

def setup(bot):
    bot.add_cog(ClickSendCallCog(bot))
