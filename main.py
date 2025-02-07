import telebot#telebot - модуль, с помощью которого мы можем создать своего телеграмм бота
import random

Madagaskar_photo = "Cringe_photos/MADAGASKAR.png"
Omnomnom = "Cringe_photos/tiktok_moment_1.mp4"

randomy = random.randint(1, 3)
Token = "7642317234:AAH7k0vGi8OgPHAl9L834la2tiKtyk_Ikn8"

bot = telebot.TeleBot(Token)

@bot.message_handler(commands=["start"])#Хендлер - это обработчик, куда мы сохраняем комманду, которую мы сможем писать боту, на которую бот будет отвечать
def start_text(message):
    bot.send_message(
        message.chat.id,
        "Вечер в хату, это бот, который захватит весь мир, заставив вас деградировать, использовав его базовые функции. Чтобы получить кринж, напишите /repost")

@bot.message_handler(commands=["repos"])
def random_joke(message):
    randomy = random.randint(1, 3)
    bot.send_message(message.chat.id, text=message)
    if randomy == 1:
        bot.send_message(
            message.chat.id,
            "Фиг тебе, я в бета тесте")
    elif randomy == 2:
        bot.send_message(message.chat.id, "Привет! Ты выиграл случайное сообщение!")
    elif randomy == 3:
        bot.send_message(message.chat.id, "Хватить спамить командой")


@bot.message_handler(commands=["repost"])
def cringe_things(message):
    overrandom = random.randint(1, 2)
    if overrandom == 1:
        with open(Madagaskar_photo, "rb") as photo:#with open - это конструкция для открытия файлов, rb - read binary - читать в двоичноимм коде(как и надо с картинками)
            bot.send_photo(message.chat.id, photo,
            caption = "Вы открыли новый кринж из тиктока - Мадагаскар! \nРедкость : редкий(2000 очков)")
    elif overrandom == 2:
        with open(Omnomnom, "rb") as video:
            bot.send_video(message.chat.id, video,
            caption = "Вы открыли новый кринж из тиктока - Рекорд! \nРедкость : обычная(1000 очков)")#send_video нужн для того, чтобы отправлять ВИДЕО<- <- <- <- <- <-



if __name__ == "__main__":
    bot.polling(non_stop=True)