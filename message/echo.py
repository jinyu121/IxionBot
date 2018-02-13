# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler


def active(dispatcher, group):
    dispatcher.add_handler(MessageHandler(Filters.text, func), group=group)


def func(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="“{}”".format(update.message.text))
