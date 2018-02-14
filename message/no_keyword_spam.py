# -*- coding: utf-8 -*-

from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoKeywordSpam(BaseMessage):
    def __init__(self):
        self.config = {
            "list": "data/keyword_spam.txt",
            'message': "",
            "delete_error": ""
        }
        super().__init__(__file__)

        self.keyword = []
        keyword_file = Path(self.config.list)
        if keyword_file.exists():
            self.keyword = [line.lower().strip() for line in keyword_file.open()]

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.group & Filters.text, self.func), group=group)

    def func(self, bot, update):
        text = update.message.text.lower()
        if any(s in text for s in self.keyword):
            if self.config.message:
                bot.send_message(chat_id=update.message.chat_id, text=self.config.message)

            if self.config.delete and "supergroup" == update.message.chat.type:
                try:
                    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
                except Exception as e:
                    if self.config.delete_error:
                        bot.send_message(chat_id=update.message.chat_id, text=self.config.delete_error)

            raise DispatcherHandlerStop()
