# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler


def active(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.status_update, func))


def func(bot, update):
    bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
