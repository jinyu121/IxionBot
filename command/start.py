# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler


def active(dispatcher):
    dispatcher.add_handler(CommandHandler("start", command))


def command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="Hello World!")
