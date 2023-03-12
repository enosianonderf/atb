import telebot
from amadeusemo import emos
from os import execv
from sys import argv, executable
from random import choice
from datetime import datetime
from amadeusph import phrases
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
que = []
emo_point = 50
ep2 = 50
current = datetime.now()

hour = current.hour
# print(current.hour)

bot = telebot.TeleBot('2008109914:AAG-L_6_JoxJbv_3PvILMwmBRB40mAiqH6k')

def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return ''.join(r)


alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'

def update():
    with open('dialogues.txt', encoding='utf-8') as f:
        content = f.read()

    blocks = content.split('\n')
    dataset = []

    for block in blocks:
        replicas = block.split('\\')[:2]
        if len(replicas) == 2:
            pair = [clean_str(replicas[0]), clean_str(replicas[1])]
            if pair[0] and pair[1]:
                dataset.append(pair)

    X_text = []
    y = []

    for question, answer in dataset[:10000]:
        X_text.append(question)
        y += [answer]

    global vectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_text)

    global clf
    clf = LogisticRegression()
    clf.fit(X, y)


update()

def get_generative_replica(text):
    global ep2, emo_point
    text_vector = vectorizer.transform([text]).toarray()[0]
    question = clf.predict([text_vector])[0]

    for i in question:
        que.append(i)

    ep = [que[-2],que[-1]]
    try:
        emo_point = int("".join(ep))
    except:
        print("No ep in learn mode.")
        emo_point = 50
        pass


    que.pop()
    que.pop()
    question = "".join(que)
    que.clear()
    print(question)
    return question

@bot.message_handler(commands=["start"])

def start(message):
    global emo_point
    emo_point = 85
    dirr = emos(emo_point)
    question = ""





    if message.from_user.username != None:
        send = "Привет, {0}, я - Макисе Курису.".format(message.from_user.first_name)
        bot.send_photo(message.chat.id, dirr)
        bot.send_message(message.chat.id, send)

    else:
        send = "Привет, я - Макисе Курису."
        emo_point = 85
        bot.send_photo(message.chat.id, dirr)
        bot.send_message(message.chat.id, send)

@bot.message_handler(commands=["testo"])
def testo(message):
    pass

@bot.message_handler(commands=["learn"])
def learn(message):
    hello = "Давай попрактикуемся на моём обучении. Напомню, что нужно ответить фраза+число. Пример : Вы круты!80\nOчки эмоции - от 0 до 25 -  ужасное, 25-50 - плохое, 50-75 -нейтральное, 75-100- счастливое.\
    10 - плач, 20 - злость, 30 - грусть, 50 - серьёзность, 55- нейтральное (стартовое) , 70 - удивление, 80 - романтика,85- лёгкая улыбка 90- смех, веселье."

    bot.send_message(message.chat.id, hello)
    #memory = open('G:/botone/atb/amadeus/singular.txt', 'br')
    #global usechatword
    #randword = [line.strip() for line in memory]
    #usechatword = choice(randword)
    # usesend = usechatword.encode('utf-8')

    #bot.send_message(message.chat.id, usechatword)
    #memory.close()
    #bot.register_next_step_handler(message, writethebrain)


# def writethebrain(message):
#     if message.text != "-1":
#         memory2 = open('G:/botone/atb/amadeus/brain.txt', 'a')
#         # usechatsend = (usechatword * chr(usechatword)).encode("utf-8")
#         memory2.write(str(message.text) + " " + str(usechatword.decode('utf-8')) + '\n')
#         memory2.close()


@bot.message_handler(content_types=["text"])
def text(message):

    print(message.text + " от " + str(message.chat.id))
    global emo_point, mtext, answ, zero
    answ = 0
    command = message.text.lower()
    if command == "не так" or command == "Не так":
        answ = 1
        bot.send_message(message.from_user.id, "а как?")
        bot.register_next_step_handler(message, wrong)

    elif "перезагрузись" in message.text.lower() or "перезапустись" in message.text.lower() or "/rrr" in message.text.lower():
        emo_point = -1
        try:
            dirr = emos(emo_point)
            bot.send_photo(message.chat.id, dirr, caption="Cейчас перезапущусь.")
            execv(executable, ['python'] + argv)
        except:
            pass

    elif "кристина" in message.text.lower():
        emo_point = 20
        mtext = "Не называй меня Кристиной!"

    elif "люблю" in message.text.lower() and "теб" in message.text.lower():
        emo_point = 75
        mtext = "Я... Я не понимаю ваши чувства."

    elif "который" in message.text.lower() and "час" in message.text.lower():
        emo_point = 80
        mtext = "Вот нынешнее время с точностью атомных часов до шестого знака после запятой : \n\n{0}".format(current)

    elif "прив" in message.text.lower() or (
            "добр" in message.text.lower() and "утро" in message.text.lower() or "вечер" in message.text.lower() or "ноч" in message.text.lower()) or "охаё" in message.text.lower():
        emo_point = 80
        trueph = phrases(hour)
        mtext = trueph

    elif "амадей" in message.text.lower() or "курису" in message.text.lower():
        emo_point = 80
        mtext = "Это должно быть моё имя."

    elif "хах" in message.text.lower():
        emo_point = 90
        mtext = "Ах-ах-ах-а!"

    elif "напиши " in message.text.lower():

        emo_point = 60
        zero = []
        try:
            for p in message.text.lower():
                zero.append(p)
            for u in range(7):
                zero.pop(0)
            mtext = "".join(zero)
            zero.clear()
        except:
            mtext = "Ошибочка."

    elif "скажи " in message.text.lower():

        emo_point = 60
        zero = []
        try:
            for p in message.text.lower():
                zero.append(p)
            for u in range(6):
                zero.pop(0)
            mtext = "".join(zero)
            zero.clear()
        except:
            mtext = "Ошибочка."


    elif "как дела" in message.text.lower() or "как твои дела" in message.text.lower() or "как у тебя дела" in message.text.lower():
        emo_point = 80
        mtext = "Спасибо, неплохо. А у вас?"

    elif "спасибо" in message.text.lower():
        emo_point = 85
        mtext = "Рада слышать, что я была полезна!"

    else:
        answ = 1
        global question
        question = command
        reply = get_generative_replica(command)
    # очки эмоции - от 0 до 25 -  ужасное, 25-50 - плохое, 50-75 -нейтральное, 75-100- счастливое.
    # 10 - плач, 20 - злость, 30 - грусть, 50 - серьёзность, 55- нейтральное (стартовое) 60- лёгкая улыбка, 70 - удивление, 80 - романтика, 90- смех, веселье.

    # memoryread = [line.strip() for line in memory]
    # if smaller in memoryread:
    # print ("О как пошла!")



    dirr = emos(emo_point)
    try:
        if answ == 1:
            bot.send_photo(message.chat.id, dirr, caption="{0}".format(str.capitalize(reply)))
        else:
            bot.send_photo(message.chat.id, dirr, caption="{0}".format(mtext))
    except:
        print(answ)
        pass
def wrong(message):
    a = f"{question}\{message.text}"
    with open('dialogues.txt', "a", encoding='utf-8') as f:
        f.write(a + "\n")
    bot.send_message(message.from_user.id, "Готово")
    update()

bot.polling(none_stop=True)
