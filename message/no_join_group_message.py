# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoJoinGroupMessage(BaseMessage):
    def __init__(self):
        self.__config = {
            "delete_error": ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.status_update, self.func), group=group)

    def func(self, bot, update):
        try:
            bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            error_message = self.config("delete_error")
            if error_message:
                bot.send_message(chat_id=update.message.chat_id, text=error_message)
        finally:
            raise DispatcherHandlerStop()
