from pydantic import SecretStr
from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    bot_token: SecretStr


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = "../.env"):
    env = Env()
    env.read_env(path)

    config = Config(
        tg_bot=TgBot(
            bot_token=env.str("BOT_TOKEN")
        )
    )
    return config
