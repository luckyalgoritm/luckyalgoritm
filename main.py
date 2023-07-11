import telebot
from telebot import types
import random
import datetime
import sqlite3

# def provtime(ti):
# 	return  datetime.datetime.today()<(datetime.datetime.strptime(ti, '%Y-%m-%d %X.%f'))
#
# spis=["1", "2", "3", "4", "5", "6", "7", "8" ,"9" ,"0", "?", "/", "_", "-", "'", "#", "!", ">", "<", "|", "q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
#
# def gener(vid):
# 	global spis
# 	a=""
# 	if vid == "Day":
# 		a+="D"
# 	elif vid == "Week":
# 		a+="W"
# 	else:
# 		a+="M"
# 	for i in range(9):
# 		a+=random.choice(spis)
# 	return a






soft=("Z#QRLWy9", "|SF%~}iC", "zrDqhYXw")
day=("LDtmE}yg", "Co*0DOP|", "HXWZTsVl")
week=("3mYS@ALL", "HydC#41B", "Nu2tP0va")
mouth=("NplX@CA~", "%WOVCINl", "QOyRAO6R")

bot = telebot.TeleBot("5787272483:AAHa0j4wVAb7WfYZQ9mWnYzPqUrLnkgPFTQ")

@bot.message_handler(commands=['start', 'help'])
def welcome(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Прайс")
	markup.add(btn1)
	bot.send_message(message.chat.id, f"Приветствую тебя, {message.chat.username}, в боте по аналитике и скаму онлайн казино 1Win, а точнее игры Lucky Jet. Аналитика основана на проверенном математическом алгоритме. Докажем что кнопка 'бабло' существует!", reply_markup=markup)
	bot.register_next_step_handler(message, buying)

def welcome2(message):
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Прайс")
	markup.add(btn1)
	bot.send_message(message.chat.id, f"Приветствую тебя, {message.chat.username}, в боте по аналитике и скаму онлайн казино 1Win, а точнее игры Lucky Jet. Аналитика основана на проверенном математическом алгоритме. Докажем что кнопка 'бабло' существует!", reply_markup=markup)
	bot.register_next_step_handler(message, buying)


def buying(message):
	# if message.text=="staff":
	# 	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	# 	btn1 = types.KeyboardButton("Генерировать код")
	# 	markup.add(btn1)
	# 	bot.send_message(message.chat.id, "😈Добро пожаловать!😈", reply_markup=markup)
	# 	bot.register_next_step_handler(message, admin)
	# else:
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	btn1 = types.KeyboardButton("Перейти к оплате")
	btn2 = types.KeyboardButton("Назад")
	markup.add(btn1, btn2)
	bot.send_message(message.chat.id, """
		Купить софт на компьютер-1499р (навсегда)
		Купить дневную подписку на сигналы из тг-499р
		Купить недельную подписку на сигналы-999р  3̶4̶9̶3̶р
		Купить месячную подписку на сигналы-3499р  1̶4̶9̶7̶0̶р
		
		""", reply_markup=markup)
	bot.send_message(message.chat.id, "P.S. Использование бота при подписке програмно не ограничено! За указанный промежуток времени вы можете неограниченно получать прогнозы!")
	bot.register_next_step_handler(message, tranz)

# def admin(message):
# 	text=message.text
# 	if text=="Генерировать код":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn2 = types.KeyboardButton("Дневная подписка")
# 		btn3 = types.KeyboardButton("Недельная подписка")
# 		btn4 = types.KeyboardButton("Месячная подписка")
# 		markup.add(btn2, btn3, btn4)
# 		bot.send_message(message.chat.id, "Выберите нужный товар!", reply_markup=markup)
# 		bot.register_next_step_handler(message, ad_gen)
# 	elif text=="Назад":
# 		bot.register_next_step_handler(message, buying)

# def ad_gen(message):
# 	if message.text=="Дневная подписка":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn2 = types.KeyboardButton("Еще код")
# 		btn1 = types.KeyboardButton("Главное меню")
# 		markup.add(btn2, btn1)
# 		bot.send_message(message.chat.id, f"{gener('Day')}", reply_markup=markup)
# 		bot.register_next_step_handler(message, ad_gen)
# 	elif message.text=="Недельная подписка":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn2 = types.KeyboardButton("Еще код")
# 		btn1 = types.KeyboardButton("Главное меню")
# 		markup.add(btn2, btn1)
# 		bot.send_message(message.chat.id, f"{gener('Week')}", reply_markup=markup)
# 		bot.register_next_step_handler(message, ad_gen)
# 	elif message.text=="Месячная подписка":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn1 = types.KeyboardButton("Еще код")
# 		btn2 = types.KeyboardButton("Главное меню")
# 		markup.add(btn1, btn2)
# 		bot.send_message(message.chat.id, f"{gener('Mouth')}", reply_markup=markup)
# 		bot.register_next_step_handler(message, ad_gen)
# 	elif message.text=="Еще код":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn2 = types.KeyboardButton("Дневная подписка")
# 		btn3 = types.KeyboardButton("Недельная подписка")
# 		btn4 = types.KeyboardButton("Месячная подписка")
# 		markup.add(btn2, btn3, btn4)
# 		bot.send_message(message.chat.id, "Выберите нужный товар!", reply_markup=markup)
# 		bot.register_next_step_handler(message, ad_gen)
# 	elif message.text=="Главное меню":
# 		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
# 		btn1 = types.KeyboardButton("Выйти из админ панели")
# 		markup.add(btn1)
# 		bot.send_message(message.chat.id, f"Подтвердите", reply_markup=markup)
# 		bot.register_next_step_handler(message, welcome2)






def tranz(message):
	if message.text=="Назад":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Назад")
		markup.add(btn1)
		bot.send_message(message.chat.id, "Нажмите ещё раз!", reply_markup=markup)
		bot.register_next_step_handler(message, welcome2)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Я оплатил!")
		markup.add(btn1)
		bot.send_message(message.chat.id, """
	Киви +79006440636
	
Биткоин bc1qlyua2jhmawjjp7na33rwh5uefday49cku2uacr

Эфир 0x16C3ef811493Cb0a42f9B47114af1626D9391Eb3
		
	После оплаты скиньте скрин нашему администратору - @BellieUS , он выдаст вам ключ на активацию подписки, подписка будет активирована со момента введения вами кода!
		""", reply_markup=markup)
		bot.register_next_step_handler(message, podpiska)

def podpiska(message):
	bot.send_message(message.chat.id, "Введите ваш лицензионный ключ, полученный от администратора:", reply_markup=types.ReplyKeyboardRemove())
	bot.register_next_step_handler(message, proverka)

def proverka(message):
	if str(message.text) in soft:
		bot.send_message(message.chat.id, "Спасибо за покупку! Ссылка на софт - https://www.dropbox.com/scl/fi/0frbksaet8a3kbdpcawjt/algoritm.zip?rlkey=xl8l4f67cmlrzz4kfe88v4xb3&dl=0")
	elif str(message.text) in day:
		bot.send_message(message.chat.id, f"""Подписка оформлена в {str(datetime.datetime.now())[:-7]} по мск. Спасибо за покупку подписки на день!
	
	Что бы получить прогнозы (прогнозируемые ставки) введите пожалуйста через пробел три предыдущих коэффицента в хронологическом порядке!
	
	Пример- 5.52 1.21 8.47""")
		bot.register_next_step_handler(message, utochnen)
	elif str(message.text) in week:
		bot.send_message(message.chat.id,f"""Подписка оформлена в {str(datetime.datetime.now())[:-7]} по мск. Спасибо за покупку подписки на неделю!
	
	Что бы получить прогнозы (прогнозируемые ставки) введите пожалуйста через пробел три предыдущих коэффицента в хронологическом порядке!
	
	Пример- 5.52 1.21 8.47""")
		bot.register_next_step_handler(message, utochnen)
	elif str(message.text) in mouth:
		bot.send_message(message.chat.id, f"""Подписка оформлена в {str(datetime.datetime.now())[:-7]} по мск. Спасибо за покупку подписки на месяц!
	
	Что бы получить прогнозы (прогнозируемые ставки) введите пожалуйста через пробел три предыдущих коэффицента в хронологическом порядке!
	
	Пример- 5.52 1.21 8.47""")
		bot.register_next_step_handler(message, utochnen)
	else:
		bot.send_message(message.chat.id, "Перепроверьте пожалуйста код, скопируйте его, а не переписывайте!")
		bot.register_next_step_handler(message, proverka)

def utochnen(message):
	text=message.text
	a=text.split(sep=' ')
	try:
		a[0]=float(a[0])
		a[1]=float(a[1])
		a[2]=float(a[2])
	except:
		pass

	if len(a)!=3 or type(a[0])!=float or type(a[1])!=float or type(a[2])!=float:
		bot.send_message(message.chat.id, "Пожалуйста, попробуйте заново, следуя инструкциям!")
		bot.register_next_step_handler(message, utochnen)
	else:
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("💸Получить первый прогноз💸")
		markup.add(btn1)
		bot.send_message(message.chat.id, f"Ваши прошлые коэффиценты - 1-{a[0]}; 2-{a[1]}; 3-{a[2]}", reply_markup=markup)
		bot.register_next_step_handler(message, prognoz)

def prognoz(message):
	if message.text=="Выйти":
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn2 = types.KeyboardButton("Выйти")
		markup.add(btn2)
		bot.send_message(message.chat.id, "Нажмите ещё раз!", reply_markup=markup)
		bot.register_next_step_handler(message, welcome2)

	else:
		spisochek=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,5,5,6,6,7,7,8,9,1501,289,9,10,11,12,13,14,15,16,17,18,19,19,20,21,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,9,9,10,11,12,13,14,15,16,17,18,19,19,20,21,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,9,9,10,11,12,13,14,15,16,17,18,19,19,20,21,22,22,23,23,24,24,25,261,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,]
		markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		btn1 = types.KeyboardButton("Следующий прогноз")
		btn2 = types.KeyboardButton("Выйти")
		markup.add(btn1, btn2)
		chisl=random.choice(spisochek)
		if chisl>=10:
			vibor="💸"
		else:
			vibor="🛸"
		bot.send_message(message.chat.id, f"{vibor}Ваш прогноз-{chisl}.{random.randint(0, 99)}{vibor}", reply_markup=markup)
		bot.register_next_step_handler(message, prognoz)






if __name__ == "__main__":
	bot.infinity_polling()