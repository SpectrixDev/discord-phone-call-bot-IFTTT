# ☎ Discord Phone Call Bot with IFTTT
[![discord.py](https://img.shields.io/badge/discord-py-red.svg)](https://github.com/Rapptz/discord.py/tree/rewrite)
[![python 3.6](https://img.shields.io/badge/python-3.6-red.svg)](https://www.python.org/)
<br>

> 🤖📞 A Discord Bot that calls your phone through a Discord command using IFTTT and Python. Simple to configure and tailor to your needs. Utilizes IFTTT's VOIP applet, which doesn't involve your personal phone number.

## ℹ Disclaimers:
1. This is not a serious project, so you may encounter bugs. If you find any, or if you require help, please open up an issue on this repo.

2. This does **not phone your phone through an actual phone number**. It uses **[IFTTT'S VOIP (click here to read more)](https://ifttt.com/voip_calls) applet**, which basically means it uses the [IFTTT](https://ifttt.com/about) app. 

## 💡 Setup

- This program was made with *Python 3.6*. Newever versions should work, but use at your own risk.
- Ensure you have [IFTTT](https://ifttt.com/about), which needs to be installed on your mobile device

#### ✅ Install the requirements

```
pip install -r requirements.txt
```

> Also, make sure you have a Discord Bot, you can make one [here](https://discordapp.com/developers/applications/). You'll need the bot token which can be found in the *bot* section of your application

#### ⚙ Configuiring IFTTT

Go to [IFTTT](https://ifttt.com/create) and create a new Applet.

For the first part, make a webhook. Name the *event name* whatever you want, but remember it.

For the second part, make a *VoIP calls* thing. **Important: Make the** ***Voice message field*** **(what the robot voice calling you will say) the following:**

```
{{Value1}} {{Value2}}
```

Next, go to https://ifttt.com/services/maker_webhooks/settings and grab the token in the **URL** section (will look something like https://maker.ifttt.com/use/**zvicdsCSDdSuDXkODmKllkOWZmwhatever** (only the gibberish part in bold)

Now go to the **config.json** file and fill in the required information. Here's what each piece means (found in config.json.example):

```json

"prefix": Used to "talk to" your bot. You can also mention the bot by default to run commands, but you also need a prefix.
"callCoolDown": Set a cooldown between how long users can use the call command. I recommend 30 seconds or more (this is per user)
"maxMsgLength": Int: The max amount of characters for the message to be read aloud over the phone call. Should be less than 2000, I recommend 250
"eventName": The event name from your webhook
"IFTTTkey": The IFTTT token/key that you got from the webhook settings URL thingy
"discordToken": Your bot token from the Discord developer portal in the bot section (NOT client secret/client ID)
```

**🎉 After filling in the information and saving, running the bot should work!**

## 🤝 Contributing and other notes

⭐Please star the repo, or even join my [Discord server](https://discord.gg/Fb8wZsn)

If you have any problems open an issue, I'll gladly help.

If you'd like to contribute, go ahead!
