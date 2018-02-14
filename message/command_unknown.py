# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from . import BaseMessage


class CommandUnknown(BaseMessage):
    def __init__(self):
        self.config = {
            'reply': False,
            'message': ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.command, self.command), group=group)

    def command(self, bot, update):
        if self.config.message:
            if self.config.reply:
                update.message.reply_text(self.config.message)
            else:
                bot.send_message(chat_id=update.message.chat_id, text=self.config.message)
