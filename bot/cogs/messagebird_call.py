from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import messagebird

class MessageBirdCallCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        cfg = bot.config
        self.access_key = cfg.get("messagebird_access_key")
        self.from_number = cfg.get("messagebird_from_number")
        self.to_number = cfg.get("messagebird_to_number")
        self.voice = cfg.get("messagebird_voice", "female")
        self.language = cfg.get("messagebird_language", "en-us")
        self.enabled = all([self.access_key, self.from_number, self.to_number])
        if self.enabled:
            self.client = messagebird.Client(self.access_key)
        else:
            self.client = None

    @commands.cooldown(1, property(lambda self: int(self.bot.config["callCoolDown"])), BucketType.user)
    @commands.command(name="messagebird_call")
    async def messagebird_call(self, ctx, *, message):
        if not self.enabled:
            await ctx.send("MessageBird integration is not configured. Please set up the required fields in config.json.")
            return

        max_length = int(self.bot.config["maxMsgLength"])
        if len(message) > max_length:
            await ctx.send(f"**{ctx.author.mention} You can't send messages over {max_length} chars long. :no_entry:**")
            return

        try:
            call_flow = self.client.voice_create_call(
                source=self.from_number,
                destination=self.to_number,
                callflow={
                    "title": "DiscordBotCall",
                    "steps": [
                        {
                            "action": "say",
                            "options": {
                                "payload": message,
                                "voice": self.voice,
                                "language": self.language
                            }
                        }
                    ]
                }
            )
            call_id = getattr(call_flow, 'id', 'unknown')
            await ctx.send(f"**MessageBird call initiated! Call ID: {call_id} :telephone_receiver:**")
        except Exception as e:
            await ctx.send(f"Failed to initiate MessageBird call: {e}")

def setup(bot):
    bot.add_cog(MessageBirdCallCog(bot))
