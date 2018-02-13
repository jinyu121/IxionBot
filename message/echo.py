# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler


def active(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.text, func))


def func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="“{}”".format(update.message.text))
