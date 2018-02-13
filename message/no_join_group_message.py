# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop


def active(dispatcher, group):
    dispatcher.add_handler(MessageHandler(Filters.status_update, func), group=group)


def func(bot, update):
    try:
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
    except Exception as e:
        pass

    raise DispatcherHandlerStop()
