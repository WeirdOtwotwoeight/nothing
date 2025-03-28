import telebot  #telebot - модуль, с помощью которого мы можем создать своего телеграмм бота
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

Madagaskar_photo = "Cringe_photos/MADAGASKAR.png"
Omnomnom = "Cringe_photos/tiktok_moment_1.mp4"
Token = "7642317234:AAH7k0vGi8OgPHAl9L834la2tiKtyk_Ikn8"
Eye = "Cringe_photos/Eye.png"
School = ["Разговоры о важном", "Алгебра", "Геометрия", "ТВиС", "Русский язык", "Английский язык", "Обществознание","География💀", "Биология", "История", "Литература", "Физика", "Информатика", "Физ-ра"]
Update_school = School.copy()
Decision = False
BFDI = False
print(Update_school)
win_opinion = ""#Переменная, в которую сохраняются выбор "пользователей" в игре с предметами
Var_one = None
Var_two = None
choose_one = None
choose_two = None
epic_two = None
chooose_one = None
chooose_two = None


bot = telebot.TeleBot(Token)


def get_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    cringe_button = KeyboardButton("Кринж с титока")
    cringer_button = KeyboardButton("Не тапайте")
    third_button = KeyboardButton("Eye of Rah")#Создаём кнопку
    button_again = KeyboardButton("вот")
    no_tap = KeyboardButton("Битва за ин")
    keyboard.add(cringe_button)
    keyboard.add(cringer_button)
    keyboard.add(third_button)#Добавляем кнопку в клавиатуру
    keyboard.add(button_again)
    keyboard.add(no_tap)
    return keyboard


@bot.message_handler(commands=[
    "start"])  #Хендлер - это обработчик, куда мы сохраняем комманду, которую мы сможем писать боту, на которую бот будет отвечать
def start_text(message):
    bot.send_message(
        message.chat.id,
        "Вечер в хату, это бот, который захватит весь мир, заставив вас деградировать, использовав его базовые функции. Чтобы получить кринж, нажмите на кнопку",
        reply_markup=get_keyboard())
    null()





@bot.message_handler(func=lambda message: message.text == "Кринж с титока")
def cringe_things(message):
    overrandom = random.randint(1, 2)
    if overrandom == 1:
        with open(Madagaskar_photo,
                  "rb") as photo:  #with open - это конструкция для открытия файлов, rb - read binary - читать в двоичноимм коде(как и надо с картинками)
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Мадагаскар! \nРедкость : редкий(2000 очков)")
    elif overrandom == 2:
        with open(Omnomnom, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Рекорд! \nРедкость : обычная(1000 очков)")  #send_video нужн для того, чтобы отправлять ВИДЕО<- <- <- <- <- <-

@bot.message_handler(func=lambda message: message.text == "Не тапайте")
def vid(message):
    bot.send_message(message.chat.id, "AAAуууэээЫЫЫ")



@bot.message_handler(func=lambda message: message.text == "Eye of Rah")#Создаю новый хендлер
def my_button(message):#Создаю функцию для своей кнопки
    with open(Eye, "rb") as photo:#Говорим программе, что сообшение - фото
        bot.send_photo(message.chat.id, photo)#Отправляем фото

def null():
    global BFDI, Var_one, Var_two, Update_school, win_opinion
    BFDI = False
    Var_one = None
    Var_two = None
    Update_school = School.copy()
    win_opinion = ""

#Хендрел сработает, когда текст сообщения будет названием предмета
@bot.message_handler(func= lambda message: message.text in School)
def user_selection_processing(message):
    global win_opinion, Update_school, Var_two, epic_two, chooose_one, chooose_two
    win_opinion = message.text
    bot.send_message(message.chat.id, f"Вы выбрали предмет {win_opinion.lower()}")
    Var_two = random.randint(0,len(Update_school))
    bot.send_message(
        
        message.chat.id,
        f"{win_opinion} или {Update_school[Var_two]}?",
        reply_markup=epic_battles
    )

    epic_two = ReplyKeyboardMarkup(resize_keyboard=True)
    chooose_one = KeyboardButton(win_opinion)
    chooose_two = KeyboardButton(Update_school[Var_two])

    epic_two.add(chooose_one)
    epic_two.add(chooose_two)


@bot.message_handler(func= lambda message: message.text == "Битва за ин")
def rogalik(message):
    global Var_two, Var_one, School, BFDI, win_opinion, Update_school, choose_one, choose_two, epic_battles

    if BFDI:
        bot.send_message(message.chat.id, "Перезапсукаем")
        null()
    else:
        BFDI = True

    Update_school = School.copy()
    bot.send_message(message.chat.id,
                     "Теперь вы оставили свою заявку на игру насмерть, от которой вы теперь не откажитесь. Короче перед вами будут 2 варианта ответа на вопрос, вы отвечаете и всe радуются жизни. Круто?")

    Var_one, Var_two = random.sample(range(13), 2)
    epic_battles = ReplyKeyboardMarkup(resize_keyboard=True)



    choose_one = KeyboardButton(School[Var_one])
    choose_two = KeyboardButton(School[Var_two])

    epic_battles.add(choose_one)
    epic_battles.add(choose_two)

    bot.send_message(
        message.chat.id,
        f"{School[Var_one]} или {School[Var_two]}?",
        reply_markup=epic_battles
    )


    if Var_one > Var_two:
        del Update_school[Var_one]#Удаляем элемент под определённым индексом
        del Update_school[Var_two]
    else:
        del Update_school[Var_two]
        del Update_school[Var_one ]  # Удаляем элемент под определённым индексом
    print(Update_school)


    return epic_two









if __name__ == "__main__":
    bot.polling(non_stop=True)
