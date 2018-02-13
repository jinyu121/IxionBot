# -*- coding: utf-8 -*-

import importlib
import logging

from telegram.ext import Updater

from util.config import Config
from util.util import get_package_class


def main():
    config = Config.get_config()
    if config.get("debug", False):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=config.token)
    dispatcher = updater.dispatcher

    for name in config.command:
        module = importlib.import_module('{}.{}'.format("command", name))
        cls = getattr(module, get_package_class(name))
        cls().active(dispatcher)

    for ith, name in enumerate(["command_unknown"] + config.message_filter):
        module = importlib.import_module('{}.{}'.format("message", name))
        module.active(dispatcher, ith)

    updater.start_polling()
    updater.idle()


if "__main__" == __name__:
    main()
