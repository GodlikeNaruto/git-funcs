from config import token
import telebot
import random

API_TOKEN = token

bot = telebot.TeleBot(API_TOKEN)

joke_list = ['''Изобрели немцы часы которые услышав мат переходили на одну минуту вперед. Решили провести эксперимент: поставят они значит часы в американский бар, французкий бар и русский заодно. И вот поставили часы в французкий бар и ушли, через день вернулись глядят часы на 3 минуты опережают. Поставили в американский бар через день вернулись опережают на 8 минут. Поставили в русский бар через день приходят часов нет спрашивают бармена где часы. А он "какие часы?". "Да вон там на стене висели" говорят немцы. "А это часы были? А я думал 
             на##й нам вентилятор зимой нужен" .(Было так много мата что стрелки часов постоянно двигались как вентилятор)''', 
            '''Была одна проблемная лошадь. отвез хозяин лошади ее к ветеринару говорит мол не двигается и не ест. Ветеринар дает таблетки и  говорит что елси через 5 дней неоклимается то уже ничем не поможешь. Первый день дали таблетку не поднимаеться. Фермер:"Наверное придется зарезать".  Свинья усливший это бежит к лошади говорит "вставай а то зарежут тебя". Лошадь не встает итак 4 дня. Пятый день лошадь встала хозяен радуется и говорит "По такому поводу зарегим свинью".''']

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['random_num'])
def send_info(message):
    bot.reply_to(message, random.randint(1, 1000))

@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = random.choice(["ОРЕЛ", "РЕШКА"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['joke'])
def send_joke(message):
    bot.reply_to(message, random.choice(joke_list))

@bot.message_handler(commands=['solve'])
def send_ans(message):
    example = message.text.split(' ')
    bot.reply_to(message, eval(example[1]))



@bot.message_handler(commands=['info', 'help'])
def send_info(message):
    bot.reply_to(message, '''This is just a personal bot of Arlott from mlbb. Nothing is intresting here. This bot has command:
                 /info - sends information about bot
                 /start - stars bots logic
                 /help - sends information about bot
                 /random_num - sends random number
                 /solve - solving the equation
                 /joke - sending a random joke
                 ''')


@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
