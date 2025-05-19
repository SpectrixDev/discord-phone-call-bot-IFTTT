import json
import os

class ConfigError(Exception):
    pass

def load_config(config_path=None):
    """
    Loads and validates the configuration from config.json.
    If config_path is not provided, defaults to ../config.json relative to this file.
    Raises ConfigError if required fields are missing.
    """
    if config_path is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        config_path = os.path.join(base_dir, "config.json")
    with open(config_path, "r") as f:
        config = json.load(f)
    required_fields = [
        "prefix", "callCoolDown", "maxMsgLength",
        "eventName", "IFTTTkey", "discordToken"
    ]
    missing = [field for field in required_fields if field not in config]
    if missing:
        raise ConfigError(f"Missing required config fields: {', '.join(missing)}")
    return config
