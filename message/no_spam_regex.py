# -*- coding: utf-8 -*-

import re
from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class NoSpamRegex(BaseMessage):
    def __init__(self):
        self.config = {
            "list": "data/spam_regex.txt",
            'message': "",
            "delete_error": ""
        }
        super().__init__(__file__)

        self.regex_list = []
        regex_file = Path(self.config.list)
        if regex_file.exists():
            self.regex_list = [re.compile(line.lower().strip(), re.IGNORECASE)
                               for line in regex_file.open()]

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.group & Filters.text, self.func), group=group)

    def func(self, bot, update):
        text = update.message.text.lower()
        if any(s.search(text) for s in self.regex_list):
            if self.config.message:
                bot.send_message(chat_id=update.message.chat_id, text=self.config.message)

            if self.config.delete and "supergroup" == update.message.chat.type:
                try:
                    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
                except Exception as e:
                    if self.config.delete_error:
                        bot.send_message(chat_id=update.message.chat_id, text=self.config.delete_error)

            raise DispatcherHandlerStop()
