# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.punish import delete_message
from util.util import send_message
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
        dispatcher.add_handler(MessageHandler(Filters.group & Filters.sticker, self.func), group=group)

    def func(self, bot, update):
        send_message(bot, update.message, self.config.message)

        if self.config.delete:
            delete_message(bot, update.message, self.config.delete_error)
            raise DispatcherHandlerStop()
