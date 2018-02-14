# -*- coding: utf-8 -*-

import re
from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.punish import delete_message
from util.util import send_message
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
            send_message(bot, update.message, self.config.message)

            if self.config.delete:
                delete_message(bot, update.message, self.config.delete_error)

            raise DispatcherHandlerStop()
