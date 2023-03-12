from random import choice


def phrases(hour):
    global trueph
    nightph = ["Время очень позднее. Почему Вы ещё не спите?",
               "Такая тихая ночь на дворе, неправда ли?",
               "Ой как спать хочется..."]
    morningph = ["Доброе утречко!",
                 "Доброго утра и хорошего Вам дня!",
                 "Эх, всё же я не выспалась. А Вы?"]
    dayph = ["Добрый день!",
             "А вот и солнышко замерло на зените.",
             "Как проходит Ваш день? Вы уже пообедали?",
             "Хорошего денёчка Вам!"]
    eveph = ["Добрый вечер.",
             "Надеюсь, вы сейчас отдыхаете! Время близится к ночи.",
             "Довольно прохладный вечерок, не так ли?"]
    if hour >= 0 and hour < 6:
        trueph = choice(nightph)
    elif hour >= 6 and hour < 12:
        trueph = choice(morningph)
    elif hour >= 12 and hour < 18:
        trueph = choice(dayph)
    elif hour >= 18 and hour <= 23:
        trueph = choice(eveph)
    return trueph
