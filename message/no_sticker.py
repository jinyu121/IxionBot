# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoSticker(BaseMessage):
    def __init__(self):
        self.__config = {
            'message': "",
            'delete': False,
            "delete_error": ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.sticker, self.func), group=group)

    def func(self, bot, update):
        warn_message = self.config('message')
        if warn_message:
            bot.send_message(chat_id=update.message.chat_id, text=warn_message)

        if self.config('delete'):
            try:
                bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            except Exception as e:
                error_message = self.config("delete_error")
                if error_message:
                    bot.send_message(chat_id=update.message.chat_id, text=error_message)
            finally:
                raise DispatcherHandlerStop()
