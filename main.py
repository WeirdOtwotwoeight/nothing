import telebot  #telebot - модуль, с помощью которого мы можем создать своего телеграмм бота
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

Madagaskar_photo = "Cringe_photos/MADAGASKAR.png"
Omnomnom = "Cringe_photos/tiktok_moment_1.mp4"
Crabs = "Cringe_photos/krabiki.mp4"
game = "Cringe_photos/those.mp4"
Tapok = "Cringe_photos/Tapok.mp4"
Intro = "Cringe_photos/pharmacy.mp4"
Eye_ = "Cringe_photos/shedevr.mp4"
Early_brainrot = "Cringe_photos/bra.mp4"
Bones = "Cringe_photos/old.mp4"
AI = "Cringe_photos/ai.mp4"
FREEDUROV = "Cringe_photos/freedurov.mp4"
Token = "7642317234:AAH7k0vGi8OgPHAl9L834la2tiKtyk_Ikn8"
Eye = "Cringe_photos/Eye.png"
Police = "Cringe_photos/black.png"
Blue = "Cringe_photos/blue_skull.png"
Yummy = "Cringe_photos/bread.png"
Dolphyn = "Cringe_photos/funny.png"
Kitchen = "Cringe_photos/goida.png"
Beaty = "Cringe_photos/gumball.png"
Hmm = "Cringe_photos/not_a_meme.png"
Avocado = "Cringe_photos/remnant.png"
Blah = "Cringe_photos/so_sad.png"
Trump = "Cringe_photos/Trump_with_Z.png"
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
all_of_them = open("dox/dox_classmates.txt", "r")
file_work = all_of_them.read()
time_one = None
time_two = None
reventure = []
dumb_dumb_dictionary = {"id":0,
                        "time":0,
                        "points":0,
                        "last_time":0}
not_none = False


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
    global all_of_them, file_work, dumb_dumb_dictionary, not_none


    bot.send_message(
        message.chat.id,
        "Вечер в хату, это бот, который захватит весь мир, заставив вас деградировать, использовав его базовые функции. Чтобы получить кринж, нажмите на кнопку",
        reply_markup=get_keyboard())


    null()


    print(message.from_user.id)
    bot.send_message(message.chat.id, message)


    all_of_them = open("dox/dox_classmates.txt", "r")
    file_work = all_of_them.read()


    if str(message.from_user.id) not in file_work:
        print(file_work)
        all_of_them = open("dox/dox_classmates.txt", "a") # Открыли файл в режиме добавления новой информации
        all_of_them.write(" ")
        all_of_them.write(str(message.from_user.id))  # Записываем новую информацию в файл
        all_of_them.write(str(message.date))
    all_of_them.close()  # Это надо делать, а не то ошибка будет


@bot.message_handler(func=lambda message: message.text == "Кринж с титока")
def cringe_things(message):
    global time_one, overrandom
    user_id = message.from_user.id
    current_time = message.date
    user_found = False

    print(reventure)

    # Проверяем, есть ли пользователь в списке
    for forr in reventure:
        if forr["id"] == user_id:
            user_found = True
            print("опять ты.")

            # Проверяем, прошло ли нужное время (4 часа = 14400 секунд)
            if current_time - forr["last_time"] >= 14400:
                # Время прошло, обновляем время и разрешаем кринж
                forr["last_time"] = current_time
                overrandom = random.randint(1, 8)  # Выбираем случайный кринж
                print("Можно выдать кринж")
            else:
                # Время не прошло, считаем сколько осталось
                remaining = 14400 - (current_time - forr["last_time"])
                hours = remaining // 3600
                minutes = (remaining % 3600) // 60

                bot.send_message(
                    message.chat.id,
                    f"Подождите еще {hours} ч. {minutes} мин. для нового кринжа"
                )
                return  # Выходим из функции, не показывая кринж
            break  # Выходим из цикла после обработки пользователя

    # Если пользователь не найден в списке
    if not user_found:
        # Создаем новую запись о пользователе
        new_user = {
            "id": user_id,
            "time": 0,
            "points": 0,
            "last_time": current_time
        }
        reventure.append(new_user)
        overrandom = random.randint(1, 16)  # Для нового пользователя разрешаем кринж

    # Отправляем кринж, если разрешено
    if overrandom == 0:
        with open(Madagaskar_photo, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Мадагаскар! \nРедкость : редкий(2000 очков)")

    elif overrandom == 1:
        with open(Crabs, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Крабики! \nРедкость : обычная(1000 очков)")
    elif overrandom == 2:
        with open(Omnomnom, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Рекорд! \nРедкость : обычная(1000 очков)")
    elif overrandom == 3:
        with open(Police, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Гамбургерная бедолага! \nРедкость : обычная(1000 очков)")
    elif overrandom == 4:
        with open(Blue, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - ужас! \nРедкость : обычная(1000 очков)")
    elif overrandom == 5:
        with open(Yummy, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Хлеб из столовки! \nРедкость : обычная(1000 очков)")
    elif overrandom == 6:
        with open(Dolphyn, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Дольфи! \nРедкость : обычная(1000 очков)")
    elif overrandom == 7:
        with open(Kitchen, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Гойда! \nРедкость : редкая(2000 очков)")
    elif overrandom == 8:
        with open(Beaty, "rb") as photo:
            bot.send_video(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Красота! \nРедкость : обычная(1000 очков)")
    elif overrandom == 9:
        with open(game, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Простая игра! \nРедкость : Редкая(2000 очков)")
    elif overrandom == 10:
        with open(Tapok, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Тапок! \nРедкость : Редкая(2000 очков)")
    elif overrandom == 11:
        with open(Intro, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Интро аптеки! \nРедкость : Эпическая(3000 очков)")
    elif overrandom == 12:
        with open(Eye_, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Райан Цикполинг! \nРедкость : Легендарная(5000 очков)")
    elif overrandom == 13:
        with open(Early_brainrot, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Эдиты, которые нам нужны! \nРедкость : Эпическая(3000 очков)")
    elif overrandom == 14:
        with open(Bones, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Машет костями! \nРедкость : Мифическая(4000 очков)")
    elif overrandom == 15:
        with open(AI, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - ИИ захватит всю землю! \nРедкость : Обычная(1000 очков)")
    elif overrandom == 16:
        with open(FREEDUROV, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - FREEDUROV! \nРедкость : Обычная(1000 очков)")
    print(reventure)





@bot.message_handler(func=lambda message: message.text == "Не тапайте")
def vid(message):
    bot.send_message(message.chat.id, "AAAуууэээЫЫЫ")



@bot.message_handler(func=lambda message: message.text == "Eye of Rah")#Создаю новый хендлер
def my_button(message):#Создаю функцию для своей кнопки
    with open(Eye, "rb") as photo:#Говорим программе, что сообшение - фото
        bot.send_photo(message.chat.id, photo)#Отправляем фото

def null():
    global BFDI, Var_one, Var_two, Update_school, win_opinion, epic_two
    BFDI = False
    Var_one = None
    Var_two = None
    Update_school = School.copy()
    win_opinion = ""
    epic_two = None


#Хендрел сработает, когда текст сообщения будет названием предмета
@bot.message_handler(func= lambda message: message.text in School)
def user_selection_processing(message):
    global win_opinion, Update_school, Var_two, epic_two, chooose_one, chooose_two
    print(Update_school)
    if len(Update_school) == 0:
        bot.send_message(message.chat.id, f"Ваш любимый предмет - это {win_opinion.lower()}")
        bot.send_message(message.chat.id, text="Напишите /start, мне лень всё делать автоматическим")
    else:

        win_opinion = message.text#Добавляем отправленное пользователем сообщение в win_opinion
        Var_two = random.randint(0, len(Update_school)-1)#Значением переменной Var_two делаем случайный индекс в диапозоне списка Update_school

        print(Update_school[Var_two])




        bot.send_message(message.chat.id, f"Вы выбрали предмет {win_opinion.lower()}")#Отправляем пользователю сообщение о его выборе


        epic_two = ReplyKeyboardMarkup(resize_keyboard=True)#Создаём клавиатуру


        epic_two.add(KeyboardButton(win_opinion))#Добавляем кнопку с выбором пользователя
        epic_two.add(KeyboardButton(Update_school[Var_two]))#Добавляем кнопку с рандомным элементом из Update_school(Его индексом является Var_two)




        bot.send_message(

            message.chat.id,
            f"{win_opinion} или {Update_school[Var_two]}?",#Отправляем сообщения с выбором
            reply_markup=epic_two#Отображаем клавиатуру
        )
        del Update_school[Var_two]#Удаляем из списка Update_school элемент с индексом Var_two


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
