# -*- coding: utf-8 -*-

import re
from telegram.ext import Filters, MessageHandler

from util.util import send_message
from util.punish import delete_message, ban_user
from util.consts import patten_muslim
from . import BaseMessage


class NoMuslim(BaseMessage):
    def __init__(self):
        self.config = {
            "delete": True,
            "delete_all": True,
            "ban": True
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(
            Filters.private & Filters.text, self.func), group=group)

    def func(self, bot, update):
        text = update.message.text.lower()
        if patten_muslim.match(text):
            if self.config.delete:
                delete_message(bot, update.message, self.config.delete_error)
            if self.config.delete_all:
                pass
            if self.config.ban:
                ban_user(bot, update.message)

            raise DispatcherHandlerStop()
