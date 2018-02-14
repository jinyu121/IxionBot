# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler

from util.util import send_message
from . import BaseCommand


class Start(BaseCommand):
    def __init__(self):
        self.config = {
            "message": "Hello World!"
        }
        super().__init__(__file__)

    def active(self, dispatcher):
        dispatcher.add_handler(CommandHandler("start", self.command))

    def command(self, bot, update):
        send_message(bot, update.message, self.config.message)
