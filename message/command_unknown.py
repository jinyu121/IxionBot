# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from . import BaseMessage


class CommandUnknown(BaseMessage):
    def __init__(self):
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.command, self.command), group=group)

    def command(self, bot, update):
        warn_message = self.config('message', "")
        if "" != warn_message.strip():
            bot.send_message(chat_id=update.message.chat_id, text=warn_message)
