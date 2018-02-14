# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.punish import delete_message
from util.util import format_with_dict
from util.util import send_message
from . import BaseMessage


class NoJoinLeftGroupMessage(BaseMessage):
    def __init__(self):
        self.config = {
            "message_join": "",
            "message_left": "",
            "delete": True,
            "delete_error": ""
        }
        super().__init__(__file__)

    def active(self, dispatcher, group):
        dispatcher.add_handler(MessageHandler(Filters.group & Filters.status_update, self.func), group=group)

    def func(self, bot, update):
        processed = False

        if update.message.new_chat_members:
            if self.config.message_join:
                for chat_member in update.message.new_chat_members:
                    text = format_with_dict(self.config.message_join, chat_member.__dict__)
                    send_message(bot, update.message, text)
                processed = True

        elif update.message.left_chat_member:
            if self.config.message_left:
                chat_member = update.message.left_chat_member
                text = format_with_dict(self.config.message_left, chat_member.__dict__)
                send_message(bot, update.message, text)
            processed = True

        if processed and self.config.delete:
            delete_message(bot, update.message, self.config.delete_error)
            raise DispatcherHandlerStop()
