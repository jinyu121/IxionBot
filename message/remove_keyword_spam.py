# -*- coding: utf-8 -*-

from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from . import BaseMessage


class RemoveKeywordSpam(BaseMessage):
    def __init__(self):
        super().__init__(__file__)

        self.keyword = []
        keyword_file = Path(self.config("list", ""))
        if keyword_file.exists():
            self.keyword = [line.strip() for line in keyword_file.open()]

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.text, self.func), group=group)

    def func(self, bot, update):

        if any(s in update.message.text for s in self.keyword):
            warn_message = self.config('message', "")
            if "" != warn_message.strip():
                bot.send_message(chat_id=update.message.chat_id, text=warn_message)

            try:
                bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
            except Exception as e:
                pass

            raise DispatcherHandlerStop()
