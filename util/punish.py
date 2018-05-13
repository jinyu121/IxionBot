# -*- coding: utf-8 -*-


def delete_message(bot, message, error_notice=""):
    if "supergroup" == message.chat.type:
        try:
            bot.delete_message(chat_id=message.chat_id, message_id=message.message_id)
        except Exception as e:
            if error_notice:
                bot.send_message(chat_id=message.chat_id, text=error_notice)


def ban_user(bot, message, error_notice=""):
    if "supergroup" == message.chat.type:
        try:
            bot.kick_chat_member(chat_id=message.chat_id,
                                 user_id=message.from_user.id)
        except Exception as e:
            if error_notice:
                bot.send_message(chat_id=message.chat_id, text=error_notice)
