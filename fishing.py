import telebot

bot = telebot.TeleBot("1583721360:AAGzZtnMGpoeYpLnX8y4DMyP0rBx4OTNjyw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "/start@fish_inPolyana_bot")

@bot . message_handler ( sticker_id = 'CAACAgIAAxkBAAL3ZmBMmFFBw_a3Pu0u4278SyWDfAm7AAKJAANVS74W5tXN6X4K-IQeBA') 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( commands=['gay?']) 
def  handle_message ( message ):
    import random 
    a = ["естественно", "нет", "ни в коем случае", "да", "может быть", "неизвестно", "и не только", "а ты проверь"]
    bot.reply_to(message,random.choice(a))

@bot . message_handler ( commands=['fishing']) 
def  handle_message ( message ):
    import random 
    a = ["карась", "окунь", "лящ", "ничего", "ничего", "сом", "ничего", "щука"]
    bot.reply_to(message,random.choice(a))

@bot . message_handler ( commands=['orel']) 
def  handle_message ( message ):
    import random 
    photo = open('решка.jpg', 'rb') 
    photo1 = open('орёл.webp', 'rb') 
    a = ["орёл", "решка"]
    if random.choice(a)== "орёл":
        bot.reply_to(message,"орёл"+"- YOU WIN")
        bot.send_sticker(message.chat.id, photo1)
    else:
        bot.reply_to(message,"решка"+"- YOU LOSE")
        bot.send_sticker(message.chat.id, photo)
@bot . message_handler ( commands=['reshka']) 
def  handle_message ( message ):
    import random 
    photo = open('решка.jpg', 'rb') 
    photo1 = open('орёл.webp', 'rb')   
    a = ["орёл", "решка"] 
    if random.choice(a)== "решка":
        bot.reply_to(message,"решка"+"- YOU WIN")
        bot.send_sticker(message.chat.id, photo)
    else:
        bot.reply_to(message,"орёл"+"- YOU LOSE")
        bot.send_sticker(message.chat.id,photo1 )
@bot . message_handler ( commands=['monetka']) 
def  handle_message ( message ):
    import random 
    photo = open('решка.jpg', 'rb') 
    photo1 = open('орёл.webp', 'rb') 
    a = ["орёл", "решка"]
    if random.choice(a)== "решка":
        bot.reply_to(message,"решка")
        bot.send_sticker(message.chat.id,photo)
    elif random.choice(a)== "орёл":
        bot.reply_to(message,"орёл")
        bot.send_sticker(message.chat.id, photo1)  
@bot . message_handler ( regexp = "его идеи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "eго идeи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "eго идеи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "его идeи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "eгo идeи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "eгo идеи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "егo идеи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

@bot . message_handler ( regexp = "егo идeи"  ) 
def  handle_message ( message ): 
    bot.reply_to(message,"Иди нахуй")

#@bot.message_handler(content_types=['sticker'])
#def sticker_id(message):
 #   if file_id =='AAMCAgADHQJWb8hgAAIBP2BPTeagJKcIO752nTaxNlzTHCZ7AAKJAANVS74W5tXN6X4K-IRmhqaaLgADAQAHbQADMh0AAh4E'
  #     bot.reply_to(message,"Иди нахуй")

bot.polling()
#@bot . message_handler ( regexp = "Марк гей?" ) 
#def  handle_message ( message ): 
 #   bot.reply_to(message,"естественно")




#CAACAgIAAxkBAAL3ZmBMmFFBw_a3Pu0u4278SyWDfAm7AAKJAANVS74W5tXN6X4K-IQeBA

#@bot.message_handler(content_types=['sticker'])
#def handle_docs_audio(message):
 #   bot.reply_to(message, "Иди нахуй")
  
#@bot.message_handler(commands=['торт'])
#def send_welcome(message):
	#bot.reply_to(sticker, "Иди нахуй")
 #   bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAL3ZmBMmFFBw_a3Pu0u4278SyWDfAm7AAKJAANVS74W5tXN6X4K-IQeBA')



#@bot.message_handler(content_types=['sticker'])
#def sticker_id(message):
    #print(message)
 #   if message.sticker.id == 'CAACAgIAAxkBAAL3ZmBMmFFBw_a3Pu0u4278SyWDfAm7AAKJAANVS74W5tXN6X4K-IQeBA':
  #      bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')
#@bot.message_handler(func='we')
#def echo_all(message):
#	bot.reply_to(message,"Иди нахуй")

#@bot.message_handler(func=lambda sticker: True)
#def echo_all(sticker):
#	bot.reply_to(sticker, sticker.text)s