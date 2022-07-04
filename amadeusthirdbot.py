import telebot
from os import listdir, path, execv
from sys import argv, executable
from random import choice, randint
emo_point = 55

bot = telebot.TeleBot('2008109914:AAG-L_6_JoxJbv_3PvILMwmBRB40mAiqH6k')

@bot.message_handler(commands=["start"])
def start(message):
    global emo_point
    if message.from_user.username != None:
        send = "Привет, {0}, я - Макисе Курису. Я ИИ, которого ты можешь обучать.".format(message.from_user.first_name)
        emo_point = 55
        if emo_point == 55:
            DIR = 'G:/botone/atb/amadeus/KurisuNeutral/'
            emo = open(path.join(DIR, choice(listdir(DIR))), 'rb')
        bot.send_photo(message.chat.id, emo)
        bot.send_message(message.chat.id, send)

    else:
        send = "Привет, я - Макисе Курису. Я ИИ, которого ты можешь обучать."
        emo_point = 55
        if emo_point == 55:
            DIR = 'G:/botone/atb/amadeus/KurisuNeutral/'
            emo = open(path.join(DIR, choice(listdir(DIR))), 'rb')
        bot.send_photo(message.chat.id, emo)
        bot.send_message(message.chat.id, send)

@bot.message_handler(commands=["learn"])


def learn(message):
    hello = "Давай попрактикуемся на моём обучении. Напомню, что нужно ответить цифрой на какое-либо слово, которое я вам пошлю."
    bot.send_message(message.chat.id, hello)
    memory = open('G:/botone/atb/amadeus/singular.txt', 'br')
    global usechatword
    randword = [line.strip() for line in memory]
    usechatword = choice (randword)
    #usesend = usechatword.encode('utf-8')

    bot.send_message(message.chat.id, usechatword)
    memory.close()
    bot.register_next_step_handler(message, writethebrain)

def writethebrain(message):
    if message.text != "-1":
        memory2 = open('G:/botone/atb/amadeus/brain.txt', 'a')
        #usechatsend = (usechatword * chr(usechatword)).encode("utf-8")
        memory2.write(str(message.text) + " " + str(usechatword.decode('utf-8')) + '\n')
        memory2.close()



@bot.message_handler(content_types=["text"])
def text(message):
    global emo_point
    #очки эмоции - от 0 до 25 -  ужасное, 25-50 - плохое, 50-75 -нейтральное, 75-100- счастливое.
    # 10 - плач, 20 - злость, 30 - грусть, 50 - серьёзность, 55- нейтральное (стартовое) 60- лёгкая улыбка, 70 - удивление, 80 - романтика, 90- смех, веселье.



    if message.text == "80":

        emo_point = 80

        mtext = "...!"
    #memoryread = [line.strip() for line in memory]
    #if smaller in memoryread:
        #print ("О как пошла!")

    elif "перезагрузись" in message.text.lower() or "перезапустись" in message.text.lower():
        emo_point = -1
        try:
            mtext = "Хорошо, сейчас я перезагружу себя."
            execv(executable, ['python'] + argv)
        except:
            pass
    #Давай мы тебя научим базовым эмоциям, Кристина.
    elif "кристина" in message.text.lower():
        emo_point = 20
        mtext = "Не называй меня Кристиной!"


    elif "привет" in message.text.lower():
        emo_point = 55
        mtext = "Здравствуйте, создатель."

    else:
        emo_point = 30
        mtext = "Извините, я ещё не умею отвечать на всё."

    if emo_point == -1:
        DIR = 'G:/botone/atb/amadeus/KurisuSleep/'
    elif emo_point == 10:
        DIR = 'G:/botone/atb/amadeus/KurisuCry/'
    elif emo_point == 20:
        DIR = 'G:/botone/atb/amadeus/KurisuAngry/'
    elif emo_point == 30:
        DIR = 'G:/botone/atb/amadeus/KurisuSad/'
    elif emo_point == 50:
        DIR = 'G:/botone/atb/amadeus/KurisuSerious/'
    elif emo_point == 55:
        DIR = 'G:/botone/atb/amadeus/KurisuNeutral/'
    elif emo_point == 60:
        DIR = 'G:/botone/atb/amadeus/KurisuSmile/'
    elif emo_point == 70:
        DIR = 'G:/botone/atb/amadeus/KurisuUdiv/'
    elif emo_point == 80:
        DIR = 'G:/botone/atb/amadeus/KurisuEmb/'
    elif emo_point == 90:
        DIR = 'G:/botone/atb/amadeus/Kurisu/Fun/'
    emo = open(path.join(DIR, choice(listdir(DIR))), 'rb')
    bot.send_photo(message.chat.id, emo)
    bot.send_message(message.chat.id, mtext)
bot.polling(none_stop=True)
