# -*- coding: utf-8 -*-

from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.config import Config

__keyword = []


def active(dispatcher, group):
    global __keyword

    config = Config.get_config("remove_keyword_spam")
    keywork_file = Path(config.get("list", ""))
    if keywork_file.exists():
        __keyword = [line.strip() for line in keywork_file.open()]

    dispatcher.add_handler(MessageHandler(Filters.text, func), group=group)


def func(bot, update):
    global __keyword
    config = Config.get_config('remove_keyword_spam')

    if any(s in update.message.text for s in __keyword):
        warn_message = config.get('message', "")
        if "" != warn_message.strip():
            bot.send_message(chat_id=update.message.chat_id, text=warn_message)

        try:
            bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            pass

        raise DispatcherHandlerStop()
