import telebot
from telebot import types
import random
bot = telebot.TeleBot('1616031630:AAFjw7CB1DoAS9wsVVL_rS9x-QzadZYkotA')

a = [[0 for i in range(2)] for j in range(24)]
a[0][1] = 1
a[0][0] = 15
a[12][1] = 2
a[12][0] = 15
key = 0
a = 0
b = 0
zar1 = 0

def throw_cube():
    cube = random.randint(1, 6)
    return cube


@bot.message_handler(commands=['start'])
def start(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
	btn1 = types.KeyboardButton('Играть черными')
	btn2 = types.KeyboardButton('Играть белыми')
	btn3 = types.KeyboardButton('Статистика')
	markup.add(btn1, btn2, btn3)
	send_mess = f"<b>Привет {message.from_user.first_name} </b>\nСыграем партейку?"
	bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def mess(message):
	get_message_bot = message.text.strip().lower()
	if get_message_bot == "играть белыми":
		zar1 =  throw_cube()
		b = throw_cube()
		bot.send_message(message.chat.id, "Вам выпало " +str(zar1) +" и "+ str(b))

		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
		btn1 = types.KeyboardButton('Пойти на '+str(zar1))
		btn2 = types.KeyboardButton('Пойти на '+str(b))
		markup.add(btn1, btn2)


		final_message = "Вывод доски"
	elif get_message_bot == "пойти на 3":
		for i in range(24):
			if a[i][1] == 1 and a[i + 3][1] != 2:
				print("Есть ход c ", i, " на ", 3)
				bot.send_message(message.chat.id, "Доступен ход с "+str(i))
				key = 1
			bot.send_message(message.chat.id, "1")

			markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
			btn1 = types.KeyboardButton('Пойти с  ')
			btn2 = types.KeyboardButton('Пойти на ' )
			markup.add(btn1, btn2)

			final_message = "Вывод доски"

	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
		btn1 = types.KeyboardButton('Создание игр')
		btn2 = types.KeyboardButton('Мобильные приложения')
		btn3 = types.KeyboardButton('Веб разработка')
		btn4 = types.KeyboardButton('Софт для компьютеров')
		btn5 = types.KeyboardButton('Обработка данных')
		btn6 = types.KeyboardButton('Создание ИИ')
		markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
		final_message = "Так, так, так\nПостой, лучше нажми на одну из интерактивных кнопок ниже"
	bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)

def get_name(message): #получаем фамилию
    global name;
    name = message.text;

    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?');
    bot.register_next_step_handler(message, get_surnme);

bot.polling(none_stop=True)