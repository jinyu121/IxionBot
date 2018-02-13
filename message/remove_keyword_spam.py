# -*- coding: utf-8 -*-

from pathlib import Path

from telegram.ext import Filters, MessageHandler

from util.config import Config

__keyword = []


def active(dispatcher):
    global __keyword

    config = Config.get_config("remove_keywork_spam")
    keywork_file = Path(config.get("list", ""))
    if keywork_file.exists():
        __keyword = [line.strip() for line in keywork_file.open()]

    dispatcher.add_handler(MessageHandler(Filters.text, func))


def func(bot, update):
    global __keyword

    if any(s in update.message.text for s in __keyword):
        bot.send_message(chat_id=update.message.chat_id, text="SPAM")
