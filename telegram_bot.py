#https://www.youtube.com/watch?v=5nhdxpoicW4&t=108s
import requests
import json
import logging

import configparser as cfg

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(levelname)s %(name)s:%(lineno)d] %(message)s",
)

LOG = logging.getLogger()

class telegram_chatbot:
    def __init__(self):
        self.token = self.read_token_from_config_file()
        print("token", self.token)
        self.base = "https://api.telegram.org/bot{}/".format(self.token)
    
    def get_updates(self,offset=None):
        LOG.info("...geting all message updates")
        url = self.base + "getUpdates?timeout=100"
        if offset:
            url = url + "&offset={}".format(offset+1)
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self,msg,chat_id,name,message):
        url = self.base + "sendMessage?chat_id={}&text={}".format(chat_id,msg)
        if msg is not None:
            try: 
                requests.get(url)
                LOG.info("replying to " + name + "'s message: " + message + "  ....  with: " + msg )
            except:
                LOG.info("replying to " + name + "'s message: " + "error!" + "  ....  with: " + msg )

    def read_token_from_config_file(self):
        parser = cfg.ConfigParser()
        config = r"resources\config.cfg"
        parser.read(config)
        return parser.get("creds","token")
