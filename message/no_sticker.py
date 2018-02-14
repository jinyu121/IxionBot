# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoSticker(BaseMessage):
    def __init__(self):
        self.config = {
            'message': "",
            'delete': False,
            "delete_error": ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.sticker, self.func), group=group)

    def func(self, bot, update):
        if self.config.message:
            bot.send_message(chat_id=update.message.chat_id, text=self.config.message)

        if self.config.delete:
            try:
                bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            except Exception as e:
                if self.config.delete_error:
                    bot.send_message(chat_id=update.message.chat_id, text=self.config.delete_error)
            finally:
                raise DispatcherHandlerStop()
