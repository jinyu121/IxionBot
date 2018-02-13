# -*- coding: utf-8 -*-

from telegram.ext import Filters, MessageHandler

from util.config import Config


def active(dispatcher, group):
    dispatcher.add_handler(MessageHandler(Filters.command, command), group=group)


def command(bot, update):
    config = Config.get_config('command_unknown')
    warn_message = config.get('message', "")
    if "" != warn_message.strip():
        bot.send_message(chat_id=update.message.chat_id, text=warn_message)
