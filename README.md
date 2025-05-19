# ☎ Discord Phone Call Bot

A modular Discord bot that can make phone calls using a variety of providers, including IFTTT, Twilio, Vonage, Plivo, ClickSend, MessageBird, and Sinch. Easily configurable and extensible for new integrations.

## Features

- Make phone calls from Discord using multiple providers.
- Modular design: each provider is a separate cog.
- Easy configuration via `config.json`.
- Cooldown and message length limits.
- Python 3.6+ compatible.

## Supported Providers & Commands

| Provider     | Command           | Description                       |
|--------------|-------------------|-----------------------------------|
| IFTTT        | `!call`           | Calls via IFTTT VoIP applet       |
| Twilio       | `!twilio_call`    | Calls using Twilio API            |
| Vonage       | `!vonage_call`    | Calls using Vonage Voice API      |
| Plivo        | `!plivo_call`     | Calls using Plivo Voice API       |
| ClickSend    | `!clicksend_call` | Calls using ClickSend TTS         |
| MessageBird  | `!messagebird_call` | Calls using MessageBird Voice   |
| Sinch        | `!sinch_call`     | Calls using Sinch Voice API       |

## Project Structure

```
.
├── bot/
│   ├── __init__.py
│   ├── config.py
│   ├── core.py
│   └── cogs/
│       ├── __init__.py
│       ├── ifttt_call.py
│       ├── twilio_call.py
│       ├── vonage_call.py
│       ├── plivo_call.py
│       ├── clicksend_call.py
│       ├── messagebird_call.py
│       └── sinch_call.py
├── config.json
├── config.json.example
├── requirements.txt
├── main.py
└── README.md
```

## Setup

1. **Clone the repository and install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

2. **Configure your bot:**
    - Copy `config.json.example` to `config.json`.
    - Fill in the required fields for the providers you want to use.
    - You must always set up your Discord bot token and a command prefix.

3. **Provider Setup:**
    - For each provider, follow their documentation to obtain API keys, tokens, and phone numbers.
    - See comments in `config.json.example` for required fields.

4. **Run the bot:**
    ```sh
    python main.py
    ```

## Example `config.json`

See `config.json.example` for all available options and documentation.

## Adding New Integrations

- Add a new cog in `bot/cogs/`.
- Document new config fields in `config.json.example`.
- Update this README with the new command.
