# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from util.util import send_message
from . import BaseMessage


class CommandUnknown(BaseMessage):
    def __init__(self):
        self.config = {
            'reply': False,
            'message': ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.command, self.command), group=group)

    def command(self, bot, update):
        send_message(bot, update.message, self.config.message, self.config.reply)
