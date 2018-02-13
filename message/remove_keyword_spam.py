# -*- coding: utf-8 -*-

from pathlib import Path

from telegram.ext import Filters, MessageHandler
from telegram.ext.dispatcher import DispatcherHandlerStop

from util.config import Config

_keyword = []


def active(dispatcher, group):
    global _keyword
    config = Config.get_config(__file__)

    keywork_file = Path(config.get("list", ""))
    if keywork_file.exists():
        _keyword = [line.strip() for line in keywork_file.open()]

    dispatcher.add_handler(MessageHandler(Filters.text, func), group=group)


def func(bot, update):
    global _keyword
    config = Config.get_config(__file__)

    if any(s in update.message.text for s in _keyword):
        warn_message = config.get('message', "")
        if "" != warn_message.strip():
            bot.send_message(chat_id=update.message.chat_id, text=warn_message)

        try:
            bot.delete_message(chat_id=update.message.chat_id, message_id=update.message.message_id)
        except Exception as e:
            pass

        raise DispatcherHandlerStop()
