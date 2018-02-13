# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoSticker(BaseMessage):
    def __init__(self):
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.sticker, self.func), group=group)

    def func(self, bot, update):
        warn_message = self.config('message', "")
        if "" != warn_message.strip():
            bot.send_message(chat_id=update.message.chat_id, text=warn_message)

        if self.config('delete', False):
            try:
                bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            except Exception as e:
                pass

            raise DispatcherHandlerStop()
