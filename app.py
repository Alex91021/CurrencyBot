import telebot
from extensions import Converter, APIException
from config import currencies, TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'START', 'Start', 'help', 'HELP', 'Help'])
def start_help(message):
    text = 'Чтобы начать работу введите команду боту в формате: \n <название валюты КОТОРУЮ нужно сконвертировать> \
<название валюты В КОТОРУЮ нужно сконвертировать> <количество конвертируемой валюты> \n Пример: USD RUB 150 \n \
 Увидеть список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['Values', 'values', 'VALUES'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты: \n'
    for currency in currencies.items():
        text = '\n'.join((text, str(currency)))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    val = message.text.split()
    try:
        if len(val) != 3:
            raise ValueError('Неверное количество параметров!')

        txt_bot = Converter.new_convert(*val)
    except ValueError as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}")
    except APIException as e:
        bot.reply_to(message, f"Ошибка в команде:\n{e}" )
    else:
        bot.reply_to(message, txt_bot)


bot.polling(none_stop=True)
