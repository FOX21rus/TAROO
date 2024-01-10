import telebot
from telebot import types

bot = telebot.TeleBot('6742400361:AAFpodIAJVdEH8hEFmXdKlI3URtqAfangrE')

#Описание команд для выполнения запросов
@bot.message_handler(commands=['start'])
def main(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Что меня ожидает сегодня?', callback_data='me')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('Моё ID', callback_data='edit')
    btn3 = types.InlineKeyboardButton('Меню помощи по боту', callback_data='help')
    markup.row(btn2, btn3)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}. <b>Я таролог, маг и предсказатель.</b> <em><u> Я использую таро-карты, чтобы предсказывать будущее и помочь людям в их жизни. Как я могу помочь?</u></em>', parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['me'])
def main(message):
        bot.send_message(message.chat.id,f'Спасибо за ваш вопрос! {message.from_user.first_name} Я проведу расклад таро, чтобы помочь вам получить ответ на ваш вопрос. Ваш расклад состоит из трех карт: 1. Карта прошлого - Колесо Фортуны2. Карта настоящего - Карта Отшельник 3. Карта будущего - Карта Солнце  Начнем с толкования первой карты - Колесо Фортуны. Эта карта может указывать на то, что в прошлом у вас были значительные изменения в жизни. Возможно, вы пережили какие-то сильные эмоциональные или финансовые колебания. Вторая карта - Карта Отшельник, указывает на то, что в настоящее время вы можете чувствовать желание уединиться и провести время в одиночестве. Это может быть время самоанализа и внутреннего роста. Наконец, третья карта - Карта Солнце, указывает на то, что в будущем вы можете ожидать новых возможностей и успеха. Эта карта предвещает яркое будущее и новые начинания, которые принесут вам радость и удовлетворение. Итак, на основании расклада таро, можно сделать вывод, что сегодня вы можете ощущать желание уединиться и провести время в одиночестве, однако будущее выглядит светлым и полным новых возможностей. Надеюсь, что это ответ помог вам! Чтобы воспользоваться детальным толкованием карт или задать дополнительные вопросы, воспользуйтесь меню.' )
@bot.message_handler(commands=['id'])
def main(message):
      bot.reply_to(message, f'ID: {message.from_user.id}')

# Описание команды для отслеживания фото видео аудио файла
@bot.message_handler(content_types=['photo', 'video', 'audio'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Удалить фото', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.reply_to(message, f'Какое красивое фото! {message.from_user.first_name} {message.from_user.last_name}', reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)


bot.polling(none_stop=True)