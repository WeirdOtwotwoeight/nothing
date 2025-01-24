import telebot#telebot - модуль, с помощью которого мы можем создать своего телеграмм бота

Black_person_from_film = "7642317234:AAH7k0vGi8OgPHAl9L834la2tiKtyk_Ikn8"

def start_text(first_message):
    bot.send_message(first_message.chat.id, "Салам алейкум, это бот, который захватит весь мир, заставив вас деградировать, использовав его базовые функции")


bot = telebot.TeleBot(Black_person_from_film)
@bot.start_text(commamds=["start"])

if __name__ == "__main__":
    bot.polling(non_stop=True)