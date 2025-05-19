import telebot  #telebot - модуль, с помощью которого мы можем создать своего телеграмм бота
import random
import os #модуль для работы с операционной системой
from telebot.types import ReplyKeyboardMarkup, KeyboardButton


print(os.name, "- имя системы")


Token = os.environ.get("BOT_TOKEN" , "7642317234:AAH7k0vGi8OgPHAl9L834la2tiKtyk_Ikn8")
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
construction = "Cringe_photos/construction.mp4"
oldest = "Cringe_photos/oldest.mp4"
Understand = "Cringe_photos/his_word.mp4"
doza = "Cringe_photos/doza.mp4"
ugh = "Cringe_photos/not_to_ugh.mp4"
Bidon = "Cringe_photos/bidon.mp4"
haha = "Cringe_photos/joke.mp4"
bluey = "Cringe_photos/president.mp4"
beast = "Cringe_photos/mr_beast.mp4"
babochka = "Cringe_photos/babochka.mp4"
Ded = "Cringe_photos/ded.mp4"
osu = "Cringe_photos/osu.mp4"
Secret = "Cringe_photos/shhh.mp4"
Aviasales = "Cringe_photos/aviasales.mp4"
Pov_peremennaya = "Cringe_photos/pov.mp4"
legend = "Cringe_photos/legend.mp4"
flop = "Cringe_photos/presentation.mp4"
WTF = "Cringe_photos/jingle.mp4"
here = "Cringe_photos/emitrump.mp4"
why = "Cringe_photos/serious.mp4"
br = "Cringe_photos/pvz.mp4"
world = "Cringe_photos/fire.mp4"
imba = "Cringe_photos/i_guess.mp4"
player = "Cringe_photos/edgar.mp4"
head = "Cringe_photos/head.mp4"
horse = "Cringe_photos/quite.mp4"
voron = "Cringe_photos/car.mp4"
second = "Cringe_photos/ai_two.mp4"
face = "Cringe_photos/face.mp4"
rizz = "Cringe_photos/skibidi.mp4"
clown_fish = "Cringe_photos/u.mp4"
chunrda = "Cringe_photos/WWW.mp4"
idk = "Cringe_photos/very_dumb.mp4"
m = "Cringe_photos/m_and_ms.mp4"
jen = "Cringe_photos/jentle.mp4"
Indiano = "Cringe_photos/y_dafag_iszathpnng.mp4"
skull = "Cringe_photos/zzz.mp4"
garlik = "Cringe_photos/garliks.mp4"
side = "Cringe_photos/me.mp4"
hole = "Cringe_photos/holy.mp4"
ele = "Cringe_photos/electro.mp4"
lebed = "Cringe_photos/so.mp4"
nn = "Cringe_photos/key.mp4"
politic = "Cringe_photos/put_in.mp4"
sinus = "Cringe_photos/bo.mp4"
push = "Cringe_photos/um.mp4"
cola = "Cringe_photos/cola.mp4"
just_why = "Cringe_photos/why.mp4"
don = "Cringe_photos/don.mp4"
they = "Cringe_photos/pid.mp4"
fun = "Cringe_photos/line.mp4"
slim = "Cringe_photos/name.mp4"
win = "Cringe_photos/febrauly.mp4"
dont = "Cringe_photos/bruuuh.mp4"
elec = "Cringe_photos/elec.mp4"
komar = "Cringe_photos/komar.mp4"
spooky = "Cringe_photos/spoon.mp4"
graf = "Cringe_photos/def.mp4"
sparta = "Cringe_photos/spart.mp4"
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
    third_button = KeyboardButton("Eye of Rah")#Создаём кнопку
    no_tap = KeyboardButton("Битва за ин")
    points_button = KeyboardButton("Топ по баллам")
    keyboard.add(cringe_button)
    keyboard.add(third_button)#Добавляем кнопку в клавиатуру
    keyboard.add(no_tap)
    keyboard.add(points_button)
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
    global time_one, overrandom, hours, minutes, user
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
                bot.send_message(message.chat.id, "Следующий кринж доступен через "+str(hours)+" часов и "+str(minutes)+" минут")


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
        overrandom = random.randint(0, 65)  # Для нового пользователя разрешаем кринж

    # Отправляем кринж, если разрешено
    if overrandom == 0:
        with open(Madagaskar_photo, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Мадагаскар! \nРедкость : редкий(2000 очков)")
        dumb_dumb_dictionary['points']+=2000
    elif overrandom == 1:
        with open(Crabs, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Крабики! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 2:
        with open(Omnomnom, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Рекорд! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 3:
        with open(Police, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Гамбургерная бедолага! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 4:
        with open(Blue, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - ужас! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 5:
        with open(Yummy, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Хлеб из столовки! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 6:
        with open(Dolphyn, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Дольфи! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 7:
        with open(Kitchen, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Гойда! \nРедкость : редкая(2000 очков)")
        dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 8:
        with open(Beaty, "rb") as photo:
            bot.send_photo(message.chat.id, photo,
                           caption="Вы открыли новый кринж из тиктока - Красота! \nРедкость : обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 9:
        with open(game, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Простая игра! \nРедкость : Редкая(2000 очков)")
        dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 10:
        with open(Tapok, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Тапок! \nРедкость : Редкая(2000 очков)")
        dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 11:
        with open(Intro, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Интро аптеки! \nРедкость : Эпическая(3000 очков)")
        dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 12:
        with open(Eye_, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Райан Цикполинг! \nРедкость : Легендарная(5000 очков)")
        dumb_dumb_dictionary['points'] += 5000
    elif overrandom == 13:
        with open(Early_brainrot, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Эдиты, которые нам нужны! \nРедкость : Эпическая(3000 очков)")
        dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 14:
        with open(Bones, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Машет костями! \nРедкость : Мифическая(4000 очков)")
        dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 15:
        with open(AI, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - ИИ захватит всю землю! \nРедкость : Обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 16:
        with open(FREEDUROV, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - FREEDUROV! \nРедкость : Обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 17:
        with open(construction, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Меня кас...! \nРедкость : Эпическая(3000 очков)")
        dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 18:
        with open(oldest, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Я самый старый человек в мире! \nРедкость : Мифическая(4000 очков)")
        dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 19:
        with open(Understand, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Во как! \nРедкость : Обычная(1000 очков)")
        dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 20:
        with open(doza, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Доза! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 21:
        with open(ugh, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Не рыгни! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 22:
        with open(Bidon, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Честная речь нечестного политика! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 23:
        with open(haha, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Высмеивание и сатира, которую многим не понять! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 24:
        with open(bluey, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Президент ОАЭ! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 25:
        with open(beast, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Мистер Бист за кадром! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 26:
        with open(babochka, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Бабочка! \nРедкость : Легендарная(5000 очков)")
            dumb_dumb_dictionary['points'] += 5000
    elif overrandom == 27:
        with open(Ded, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - О нет! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 28:
        with open(osu, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Осуждаю! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 29:
        with open(Secret, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Государственная тайна! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 30:
        with open(Aviasales, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Авиасейлс! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 31:
        with open(Pov_peremennaya, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пов:кринж из тиктока! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 32:
        with open(legend, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Видео из тиктока 2023-его года(оно крутое)! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 33:
        with open(flop, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Да!!! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 34:
        with open(WTF, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Что это?! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 35:
        with open(here, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Трампминем! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 36:
        with open(flop, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Да!!! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 37:
        with open(why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Можно ли мустурбировать на ЕГЭ?! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 38:
        with open(br, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Бвыээувувувуа! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 39:
        with open(world, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Мир горит! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 40:
        with open(imba, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Просто шедевр, заслуживает эпика! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 41:
        with open(player, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Мои рандомы в каждой катке! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 42:
        with open(head, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Дикая морская природа! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 43:
        with open(horse, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Лизе понравится! \nРедкость : Легендарная(5000 очков)")
            dumb_dumb_dictionary['points'] += 5000
    elif overrandom == 44:
        with open(voron, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Хз! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 45:
        with open(second, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - ИИ ЗАХВАТИТ ВЕСЬ МИР! \nРедкость : Легендарная(5000 очков)")
            dumb_dumb_dictionary['points'] += 5000
    elif overrandom == 46:
        with open(face, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - faces! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 47:
        with open(rizz, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Вы не поймёте, но это имба! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 48:
        with open(clown_fish, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Рыба клоун! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 49:
        with open(chunrda, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Чундра! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 50:
        with open(idk, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Кринжапов! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 51:
        with open(m, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - m ans m's! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 52:
        with open(jen, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Лёше понравится! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 53:
        with open(Indiano, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Индийский сериал! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 54:
        with open(skull, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пиздец! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 55:
        with open(garlik, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Гарлики Харламовы! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 56:
        with open(side, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Кто такоц Себя?! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 57:
        with open(hole, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Holy fuck! \nРедкость : Легендарная(5000 очков)")
            dumb_dumb_dictionary['points'] += 5000
    elif overrandom == 58:
        with open(ele, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Электрогенератор! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 59:
        with open(lebed, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Артемий Лебедев говорит факты! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 60:
        with open(nn, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Страшно! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 61:
        with open(politic, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Обращение президента! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 62:
        with open(sinus, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Бо Синн в соло! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 63:
        with open(push, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Это важно! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 64:
        with open(cola, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Реклама Кока Колы! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 66:
        with open(don, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Великий человек говорит великие слова о великой реке! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 67:
        with open(they, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Все на свете...! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 68:
        with open(fun, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Смехуятина! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 69:
        with open(slim, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Эминем в большом 2025! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 70:
        with open(win, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Февраль побеждает! \nРедкость : Обычная(1000 очков)")
            dumb_dumb_dictionary['points'] += 1000
    elif overrandom == 71:
        with open(dont, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Хуйня какая-то! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 72:
        with open(elec, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Все стулья к 2030-ому году должны стать электрическими! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 73:
        with open(komar, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Прекрасный рингтон! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 74:
        with open(spooky, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пиздец страшно! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 75:
        with open(graf, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Задефал, как графиня! \nРедкость : Мифическая(4000 очков)")
            dumb_dumb_dictionary['points'] += 4000
    elif overrandom == 76:
        with open(sparta, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Это Спарта! \nРедкость : Редкая(2000 очков)")
            dumb_dumb_dictionary['points'] += 2000
    elif overrandom == 77:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    elif overrandom == 65:
        with open(just_why, "rb") as video:
            bot.send_video(message.chat.id, video,
                           caption="Вы открыли новый кринж из тиктока - Пачиму патрек тупой! \nРедкость : Эпическая(3000 очков)")
            dumb_dumb_dictionary['points'] += 3000
    print(reventure)
    if dumb_dumb_dictionary["points"] < 5000:
        bot.send_message(message.chat.id, f"Ваше количество очков: {dumb_dumb_dictionary["points"]}, вы пока что лох")
    elif dumb_dumb_dictionary["points"] < 10000:
        bot.send_message(message.chat.id, f"Ваше количество очков: {dumb_dumb_dictionary["points"]}, ну неплохо")
    elif dumb_dumb_dictionary["points"] < 20000:
        bot.send_message(message.chat.id,
                         f"Ваше количество очков: {dumb_dumb_dictionary["points"]}, твой мозг, наверное, уже сдеградировал до состояния овоща")
    elif dumb_dumb_dictionary["points"] < 50000:
        bot.send_message(message.chat.id,
                         f"Ваше количество очков: {dumb_dumb_dictionary["points"]}, ты там будильник ставишь что-ли?")
    elif dumb_dumb_dictionary["points"] < 100000:
        bot.send_message(message.chat.id,
                         f"Ваше количество очков: {dumb_dumb_dictionary["points"]}, вот ты каждый день по несколько раз заходишь в телеграмм, в этот чат и нажимаешь на кнопку, чтобы увидеть видео или фото, которое ты видел уже тысячи раз ради того, чтобы быть лучше своих одноклассников в дегродном боте, зависящим от удачи, а весь твой прогресс удалится через несколько недель, тебе нормально так живётся?")

    print(dumb_dumb_dictionary)
    file = open("dox/dox_classmates.txt", "a", encoding="utf-8")
    file.write( str(dumb_dumb_dictionary["points"])+" количество баллов "+str(dumb_dumb_dictionary["id"])+" ")
    file.close()






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


@bot.message_handler(func= lambda message : message.text == "Топ по баллам")
def points__(message):
    global dumb_dumb_dictionary





if __name__ == "__main__":
    bot.infinity_polling(timeout=10, long_polling_timeout=5)
#timeout защищает от зависания бота при плохом соедении с интернетом, ожидание ответа на уже отправленный запрос
#long_polling_timeout оптимизирует частоту запросов