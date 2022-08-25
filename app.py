import json
import telebot
import requests


TOKEN = '5452760990:AAGHxYTMkA0545BG-1LF8IGDaS5kD30I3Fo'
headers = {"apikey": "wSAiPyUjIkMtozybPJmVHKv1v4GgqPyd"}

bot = telebot.TeleBot(TOKEN)

keys = {'доллар': 'USD',
        'евро': 'EUR',
        'рубль': 'RUB'}

#print(keys.get('доллар'))

# base = 'USD'
# qoute = 'RUB'
# amount = 1


@bot.message_handler(commands=['start', 'START', 'Start', 'help', 'HELP', 'Help'])
def start_help(message):
    text = 'Чтобы начать работу введите команду боту в формате: \n <название валюты КОТОРУЮ нужно сконвертировать> \
<название валюты В КОТОРУЮ нужно сконвертировать> <количество конвертируемой валюты> \n Пример: доллар рубль 150 \n \
 Увидеть список доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['Values', 'values', 'VALUES'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    base, qoute, amount = message.text.split()
    r = requests.get(f"https://api.apilayer.com/fixer/convert?"
                     f"from={keys[base]}&to={keys[qoute]}&amount={amount}",
                     headers=headers)
    text = json.loads(r.content)['result']
    bot.send_message(message.chat.id, f'Цена {amount} {base} в {qoute}: {text}')





# url = "https://api.apilayer.com/fixer/convert?from={qoute}&to={base}&amount={amount}"
#
# payload = {}
# headers = {"apikey": "wSAiPyUjIkMtozybPJmVHKv1v4GgqPyd"}
#
# response = requests.request("GET", url, headers=headers, data = payload)
#
# status_code = response.status_code
# result = response.text

#


bot.polling(none_stop=True)


