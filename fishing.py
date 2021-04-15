import telebot

bot = telebot.TeleBot("1583721360:AAGzZtnMGpoeYpLnX8y4DMyP0rBx4OTNjyw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "/start@fish_inPolyana_bot")


bot.polling()
