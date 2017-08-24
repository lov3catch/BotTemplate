# -*- coding: utf-8 -*-
from telegram.ext import MessageHandler

from handlers.decorators import save_chanel_decorator


@save_chanel_decorator
def echo(bot, update):
    bot.send_message(update.message.chat.id, update.message.text)


def init_handlers(dispatcher):
    dispatcher.add_handler(MessageHandler(None, echo))
    return dispatcher
