# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from util.config import Config


def active(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.sticker, func))


def func(bot, update):
    config = Config.get_config('no_sticker')

    warn_message = config.get('message', "")
    if "" != warn_message.strip():
        bot.send_message(chat_id=update.message.chat_id, text=warn_message)

    if config.get('delete', False):
        bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
