# -*- coding: utf-8 -*-

import importlib
import logging

from telegram.ext import Updater

from util.config import Config


def main():
    config = Config.get_config()
    if config.get("debug", False):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=config.token)
    dispatcher = updater.dispatcher

    for name in config.command:
        module = importlib.import_module('{}.{}'.format("command", name))
        module.active(dispatcher)

    for name in config.message_filter + ["command_unknown"]:
        module = importlib.import_module('{}.{}'.format("message", name))
        module.active(dispatcher)

    updater.start_polling()


if "__main__" == __name__:
    main()
