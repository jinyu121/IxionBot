# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from util.util import send_message
from . import BaseMessage


class Echo(BaseMessage):
    def __init__(self):
        self.config = {
            "format": "{}",
            "reply": False
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.private & Filters.text, self.func), group=group)

    def func(self, bot, update):
        text = self.config.format.format(update.message.text)
        send_message(bot, update.message, text, self.config.reply)
