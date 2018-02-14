# -*- coding: utf-8 -*-

from collections import defaultdict


def get_package_class(name):
    name = [x.capitalize() for x in name.split("_")]
    return "".join(name)


def format_with_dict(format_string, content_dict):
    return format_string.format_map(defaultdict(str, **content_dict))


def send_message(bot, message, text, reply=False):
    if text:
        if reply:
            message.reply_text(text)
        else:
            bot.send_message(chat_id=message.chat_id, text=text)
