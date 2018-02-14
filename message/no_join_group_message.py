# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.punish import delete_message
from util.util import format_with_dict
from util.util import send_message
from . import BaseMessage


class NoJoinGroupMessage(BaseMessage):
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
        if update.message.new_chat_members:
            if self.config.message:
                for new_chat_member in update.message.new_chat_members:
                    text = format_with_dict(self.config.message, new_chat_member.__dict__)
                    send_message(bot, update.message, text)

            if self.config.delete:
                delete_message(bot, update.message, self.config.delete_error)
                raise DispatcherHandlerStop()
