# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from . import BaseMessage


class Echo(BaseMessage):
    def __init__(self):
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.text, self.func), group=group)

    def func(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="“{}”".format(update.message.text))
