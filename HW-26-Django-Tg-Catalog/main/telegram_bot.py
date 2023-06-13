from django.conf import settings
from telegram import Bot


async def send_telegram_notification(message):
    bot_token = settings.TELEGRAM_BOT_TOKEN
    chat_id = 534789925
    bot = Bot(token=bot_token)
    await bot.send_message(chat_id=chat_id, text=message)