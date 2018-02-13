# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.config import Config


def active(dispatcher, group):
    dispatcher.add_handler(MessageHandler(Filters.sticker, func), group=group)


def func(bot, update):
    config = Config.get_config(__file__)

    warn_message = config.get('message', "")
    if "" != warn_message.strip():
        bot.send_message(chat_id=update.message.chat_id, text=warn_message)

    if config.get('delete', False):
        try:
            bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            pass

        raise DispatcherHandlerStop()
