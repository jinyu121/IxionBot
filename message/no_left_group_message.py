# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.util import keyword_format
from . import BaseMessage


class NoLeftGroupMessage(BaseMessage):
    def __init__(self):
        self.config = {
            "message": "",
            "delete": True,
            "delete_error": ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.group & Filters.status_update, self.func), group=group)

    def func(self, bot, update):
        if update.message.left_chat_member:
            if self.config.message:
                new_chat_member = update.message.left_chat_member
                text = keyword_format(self.config.message, new_chat_member.__dict__)
                bot.send_message(chat_id=update.message.chat_id, text=text)

            if self.config.delete and "supergroup" == update.message.chat.type:
                try:
                    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
                except Exception as e:
                    if self.config.delete_error:
                        bot.send_message(chat_id=update.message.chat_id, text=self.config.delete_error)
                finally:
                    raise DispatcherHandlerStop()
