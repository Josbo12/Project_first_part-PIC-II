from Channel import Channel

import telepot


class BeerBoot(telepot.Bot):
    """BeerBoot is my telegram bot"""
    def __init__(self, token, usuaris):
        super(BeerBoot, self).__init__(token)
        self.clist = None
        self.chat_id = None
        self.users = usuaris


    def set_list(self, clist):
        self.clist = clist

    def on_chat_message(self, msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type == 'text':
            command = msg['text']
            print msg['from']['id']
            if msg['from']['id'] in self.users:
                if self.clist is not None:
                    self.clist.append(command)
                    self.chat_id = chat_id
            else:
                print "No autoritzat!"

    def respond(self,response):
        if self.chat_id is not None:
            self.sendMessage(self.chat_id, response)



class TelegramChannel(Channel):
    """Channel class, received commands from telegram"""
    def __init__(self, cfgtel=None, name="TelegramChannel"):
        super(TelegramChannel, self).__init__(cfgtel, name)
        token = self.cfgtel["telegram"]["token"]
        self.bot = BeerBoot(token, self.cfgtel["telegram"]["usuaris"])
        self.messages = []
        self.bot.set_list(self.messages)
        self.bot.notifyOnMessage()

    def get_msg(self):
        if self.msg_avail():
            return self.messages.pop(0)

    def msg_avail(self):
        return len(self.messages) > 0

    def respond(self, response):
        if response is None:
            response = "Usuari no registrat"
        self.bot.respond(response)
