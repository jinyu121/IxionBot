# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler


def active(dispatcher):
    dispatcher.add_handler(MessageHandler(Filters.command, command))


def command(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="不要调戏机器人！")
