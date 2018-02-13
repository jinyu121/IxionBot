# -*- coding: utf-8 -*-

from telegram.ext import CommandHandler

from . import BaseCommand


class Start(BaseCommand):
    def __init__(self):
        super().__init__(__file__)

    def active(self, dispatcher):
        dispatcher.add_handler(CommandHandler("start", self.command))

    def command(self, bot, update):
        bot.send_message(chat_id=update.message.chat_id, text="Hello World!")
