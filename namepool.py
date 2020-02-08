import random
import re

DICTFILE = '/usr/share/dict/words'
VALID_NAME_PATTERN = r'^[A-Z]\w{1,8}$'
VALID_PART_PATTERN = r'^\w{1,4}$'
VALID_WORD_PATTERN = r'^\w{2,12}$'
fullwordpool = []
namepool = []
wordpool = []

def draw():
    if len(wordpool) == 0:
        load_words()
    return (random.choice(wordpool) + random.choice(wordpool)).upper()

def draw_dict_sample():
    if len(fullwordpool) == 0:
        load_words()
    for _ in range(20):
        w = random.choice(fullwordpool)
        print(w.upper())

def draw_proper_noun():
    if len(namepool) == 0:
        load_words()
    return (random.choice(namepool)).upper()

def is_valid_name(w):
    return re.fullmatch(VALID_NAME_PATTERN, w)

def is_valid_part(w):
    return re.fullmatch(VALID_PART_PATTERN, w)

def is_valid_word(w):
    return re.fullmatch(VALID_WORD_PATTERN, w)

def load_words():
    global fullwordpool, namepool, wordpool
    with open(DICTFILE, 'r') as dictfile:
        words = dictfile.read().splitlines()
        fullwordpool = list(filter(is_valid_word, words))
        namepool = list(filter(is_valid_name, words))
        wordpool = list(filter(is_valid_part, words))


if __name__ == '__main__':
    # print(draw())
    # print(draw_proper_noun())
    draw_dict_sample()