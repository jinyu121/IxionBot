# -*- coding: utf-8 -*-

import importlib
import logging

from argparse import ArgumentParser
from telegram.ext import Updater

from util.config import Config
from util.util import get_package_class


def main(args):
    Config.load_config(filename=args.config)
    config = Config.get_config()

    if args.debug:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    updater = Updater(token=config.token)
    dispatcher = updater.dispatcher

    for name in config.command:
        module = importlib.import_module('{}.{}'.format("command", name))
        cls = getattr(module, get_package_class(name))
        cls().active(dispatcher)

    for ith, name in enumerate(["command_unknown"] + config.message_filter):
        module = importlib.import_module('{}.{}'.format("message", name))
        cls = getattr(module, get_package_class(name))
        cls().active(dispatcher, ith)

    logging.info("Running... Press `Ctrl+C` to stop")
    updater.start_polling()
    updater.idle()
    logging.info("Stoped")


if "__main__" == __name__:
    parser = ArgumentParser()
    parser.add_argument('--debug', '-d', action="store_true", help='Debug Mode')
    parser.add_argument('--config', '-c', default='config.yml', help='Config file')
    args = parser.parse_args()

    main(args)
