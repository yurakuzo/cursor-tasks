from telegram import Bot
import requests
from telegram.ext import Updater, CommandHandler


bot_token = '5996744927:AAHAA4KUdnLYUkox2XY_rBX-ZWnsYOKAwSs'
chat_id = 534789925
bot = Bot(token=bot_token)
api_endpoint = "https://a706-176-227-245-52.ngrok-free.app/api/v2/products/"


async def send_telegram_notification(message):
    await bot.send_message(chat_id=chat_id, text=message)


def send_product_catalog(chat_id=chat_id):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        products = response.json()
        message = ""
        for product in products:
            message += f"Title: {product['title']}\n"
            message += f"Description: {product['description']}\n"
            message += f"Price: {product['price']}\n"
        bot.send_message(chat_id=chat_id, text=message)
    else:
        bot.send_message(chat_id=chat_id, text="Failed to retrieve the product catalog.")

def main():
    import telegram

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="It's my bot, Hello")

    def catalog(update, context):
        send_product_catalog(chat_id=update.effective_chat.id)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("catalog", catalog))
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

