from pprint import pprint
import random
import math

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

    return  {
        "offset": previous_value["offset"] + offset_change,
        "score": {
            "home": previous_value["score"]["home"] + home_score_change,
            "away": previous_value["score"]["away"] + away_score_change
        }
    }
hom = []
awa = []
offse = []
def generate_game():
    stamps = [INITIAL_STAMP, ]
    current_stamp = INITIAL_STAMP
    for _ in range(TIMESTAMPS_COUNT):
        current_stamp = generate_stamp(current_stamp)
        stamps.append(current_stamp)
        hom.append(current_stamp["score"]["home"])
        awa.append(current_stamp["score"]["away"])
        offse.append(current_stamp["offset"])
    return stamps
game_stamps = generate_game()
pprint(game_stamps)

offset = int(input())

def get_score(game_stamps,offset):
    r = True
    away = 0
    home = 0
    offset1 = offset
    if offset1 > 50000:
        offset1 = 49999
    if offset > offse[-1]:
        offset = offse[-1]
    while r:
        if offset <= 0:
            r = False
        elif offse[offset1] > offset:
            offset1 -= 1
        elif offse[offset1] <= offset:
            home = hom[offset1]
            away = awa[offset1]
            r = False
    return home, away
pprint(get_score(game_stamps,offset))




