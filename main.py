import logging
from telegram_bot import telegram_chatbot
import sys
import json
import numpy as np

from src.chatbot import predict_class, get_response

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(levelname)s %(name)s:%(lineno)d] %(message)s",
)

LOG = logging.getLogger()

update_id = None
bot = telegram_chatbot()
intents = json.loads(open(r"src\intents.json").read())

# # for making simple strict responses
# def make_reply(message,updates):
#     if message is not None:
#         for item in updates:
#             name = item["message"]["from"]["first_name"]
#         reply = "Hi there " + str(name) + " how are you doing?"
#     return reply


while True:
    LOG.info("Telegram Bot is booting up!")
    updates = bot.get_updates(offset=update_id)
    # LOG.info(f"Gotten updates: {updates}")
    if updates["error_code"]:
        LOG.info(f'Server error:{updates["error_code"]}')
        sys.exit()
        
    updates = updates["result"]
    if updates:
        for item in updates:
            update_id = item["update_id"]
            try:
                message = item["message"]["text"]
            except:
                message = None
            from_ = item["message"]["from"]["id"]
            name = item["message"]["from"]["first_name"]
    
        try:
            ints = predict_class(message)
            reply = get_response(ints,intents)
            # reply = make_reply(message,updates)
            bot.send_message(reply,from_,name,message)

        except Exception:
            reply = "Error,Error! Do not Compute sticker!"
            bot.send_message(reply,from_,name,message)
            continue
        
