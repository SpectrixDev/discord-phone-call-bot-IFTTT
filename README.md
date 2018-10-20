# discord-phone-call-bot-IFTTT
> Let users call your actual phone through Discord using IFTTT and Python. Easy to set up and customize, 
> Python 3.6.5+ is required, consider upgrading tho if you haven't already

To begin, make sure you have the freshest version of discord.py. You can install this by doing the following:

```bash
pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]
```

Ensure you also have asyncio

```bash
pip3 install asyncio
```

Next, go to https://ifttt.com/create and create a new Applet.

For the first part, make a webhook. Name the *event name* whatever you want, but remember it.

For the second part, make a *VoIP calls* thing. **Important: Make the** ***Voice message field*** **(what the robot voice calling you will say) the following:**

```bash
{{Value1}} {{Value2}}
```

Next, go to https://ifttt.com/services/maker_webhooks/settings and grab the token in the **URL** section (will look something like https://maker.ifttt.com/use/zvicdsCSDdSuDXkODmKllkOWZmwhatever (only the gibbirish part)

After that, make sure you have a Discord Bot, you can make one [here](https://discordapp.com/developers/applications/). You'll need the bot token which can be found in the *bot* section of your application

Now go to the **config.json** file and fill in the required information. Here's what each piece means:

```bash
ALL BELOW ARE REQUIRED

"prefix": Used to "talk to" your bot. You can also mention the bot by default to run commands, but you also need a prefix.
"callCoolDown": Set a cooldown between how long users can use the call command. I recommend 30 seconds or more (this is per user)
"eventName": The event name I told you to remember earlier from your webhook
"IFTTTkey": The IFTTT token/key that you got from the webhook settings URL thingy
"discordToken": Your bot token from the Discord developer portal in the bot section (NOT client secret/client ID)
```

After filling in the information and saving, running the bot should work!

> Please star the repo, or even join my [Discord server](https://discord.gg/SuN49rm/) ;)

If you have any problems open an issue or join the server and I'll gladly help!
