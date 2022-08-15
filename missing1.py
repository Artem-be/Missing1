from pprint import pprint
import random
import math
import string
import re
TIMESTAMPS_COUNT = 50000

PROBABILITY_SCORE_CHANGED = 0.0001

PROBABILITY_HOME_SCORE = 0.45

OFFSET_MAX_STEP = 3

INITIAL_STAMP = {
    "offset": 0,
    "score": {
        "home": 0,
        "away": 0
    }
}


def generate_stamp(previous_value):
    score_changed = random.random() > 1 - PROBABILITY_SCORE_CHANGED
    home_score_change = 1 if score_changed and random.random() > 1 - \
        PROBABILITY_HOME_SCORE else 0
    away_score_change = 1 if score_changed and not home_score_change else 0
    offset_change = math.floor(random.random() * OFFSET_MAX_STEP) + 1

    return {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }

offset = int(input())
def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP

    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)

    return stamps 

game_stamps = generate_game()
pprint(game_stamps)

def get_score(game_stamps, offset):
    a = len(game_stamps)
    #Переводим в строку
    str1 = " ".join(map(str, game_stamps))
    #Удаляем все знаки
    for p in string.punctuation:
        if p in str1:
            b = str1.replace(p, '')
    #Выводим и сохраняем все числа
    result = " ".join(re.findall("\d+", str1))
    #Создаём список
    spisok = [int(x) for x in result.split()]
    
    #Переменные 
    offset2 = []
    home = []
    away = []
    offset3 = 0
    home1 = 1
    away1 = 2
    TR_FL = True
    END = "END"
    for i in range(a):
        offset2.append(spisok[offset3])
        offset3 += 3

        home.append(spisok[home1])
        home1 += 3
        
        away.append(spisok[away1])
        away1 += 3
        
    #Поиск и Вывод (Условия) 
    offse = offset
    if offset > TIMESTAMPS_COUNT:
        offse = TIMESTAMPS_COUNT
    while TR_FL:
        if offset < offset2[offse]:
            offse -= 1
        if offset >= offset2[offse]:
            print("Offset", ":", offset2[offse], "Score_home", ":", home[offse], "Score_away", ":", away[offse])
            print("Продолжаем поиск?", "Yes", "No")
            poisk = input()
            if poisk == "Y" or poisk == "Yes" or poisk == "y" or poisk == "yes":
                offset = int(input())
                if offset > TIMESTAMPS_COUNT:
                    offse = TIMESTAMPS_COUNT
                else:
                    offse = offset
            elif poisk != "Y" or poisk != "Yes" or poisk != "y" or poisk != "yes":
                TR_FL = False
    return END
score = get_score(game_stamps, offset)
pprint(score)



          



 
