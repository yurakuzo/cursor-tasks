import base64
from io import BytesIO
from PIL import Image
import tempfile

from telegram import Bot
import requests
from telegram.ext import Updater, CommandHandler


bot_token = '5996744927:AAHAA4KUdnLYUkox2XY_rBX-ZWnsYOKAwSs'
chat_id = 534789925
bot = Bot(token=bot_token)
api_endpoint = "https://95ab-95-47-56-193.ngrok-free.app/api/products/"


def decode_photo(code):
    _, imgstr = code.split(';base64,')
    data = base64.b64decode(imgstr)
    return Image.open(BytesIO(data))


def send_product_catalog(chat_id=chat_id):
    response = requests.get(api_endpoint)
    if response.status_code == 200:
        products = response.json()
        for product in products:
            img_data = product['image']
            image = decode_photo(img_data)
            
            caption = f"Title: {product['title']}\n"
            caption += f"Description: {product['description']}\n"
            caption += f"Price: {product['price']}\n"
            
            with tempfile.NamedTemporaryFile(suffix='.jpg') as temp:
                image.save(temp.name)
                bot.send_photo(chat_id=chat_id, caption=caption, photo=open(temp.name, 'rb'))
    else:
        bot.send_message(chat_id=chat_id, text="Failed to retrieve the product catalog.")

def main():

    updater = Updater(bot_token, use_context=True)
    dispatcher = updater.dispatcher

    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="It's my bot, Hello")

    def catalog(update, context):
        send_product_catalog(chat_id=update.effective_chat.id)

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("catalog", catalog))
    
    # loop = asyncio.get_event_loop()
    # try:
    #     loop.create_task(updater.start_polling())
    #     loop.run_forever()
    # finally:
    #     loop.stop()
    #     loop.close()
    
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
