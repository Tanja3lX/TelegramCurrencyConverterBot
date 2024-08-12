import telebot
from config import keys
from Exceptions import APIException, CryptoConverter
from API_KEYS import TOKEN

bot = telebot.TeleBot(TOKEN)

# Erstellt und aktiviert man eine virtuelle Umgebung, damit die Pakete andere Projekte nicht beeinträchtigen.
# den Dekorator verwenden
@bot.message_handler(commands=['start'])
def start(message: telebot.types.Message):
    text = (
        'To get started, enter a command in the following format:\n'
        '\n'
        'Amount of currency 😊\n'
        'Currency name 💰\n'
        'Name of the currency whose rate you would like to know 🌟\n'
        '\n'
        'Available currencies: /values\n'
        'Additionally: /support 💻'
    )
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Available currencies:\n'
    text += '\n'.join(keys.keys())
    bot.reply_to(message, text)

@bot.message_handler(commands=['support'])
def support(message: telebot.types.Message):
    text = (
        'If you encounter a problem or find a bug,\n'
        'you can contact our support team junetatsiana@gmail.com 👩‍💻'
    )
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text'])
def get_price(message: telebot.types.Message):
    try:
        values = message.text.split()
        if len(values) != 3:
            raise APIException('Incorrect number of arguments.\nInput example: 3 euro dollar')

        amount, base, quote = values
        quote = quote.lower()
        base = base.lower()

        total_base = CryptoConverter.get_price(base, quote, amount)
    except APIException as e:
        bot.reply_to(message, f'{e}')
    except Exception as e:
        bot.reply_to(message, f'Server error occurred.\n{e}')
    else:
        text = f'Price of {amount} {base} in {quote} is {total_base}'
        bot.send_message(message.chat.id, text)

# um einen Bot mit der Polling-Methode zu starten
bot.polling(none_stop=True)
