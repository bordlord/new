import telebot

bot = telebot.TeleBot('1127320220:AAFAqMnqePCfmqT7H_kCMpfWhQLCqnNRKW0')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True, True)
keyboard1.row('Сука', 'Блять', 'Пизда', 'Нахуй')
keyboard1.row('Сука', 'Блять', 'Пизда', 'Нахуй')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')

bot.polling()