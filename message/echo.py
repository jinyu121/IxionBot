# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

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

        if self.config.reply:
            update.message.reply_text(text)
        else:
            bot.send_message(chat_id=update.message.chat_id, text=text)
