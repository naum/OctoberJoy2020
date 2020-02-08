import random
import re

DICTFILE = '/usr/share/dict/words'
VALID_NAME_PATTERN = r'^[A-Z]\w{1,8}$'
VALID_WORD_PATTERN = r'^\w{1,4}$'
namepool = []
wordpool = []

def draw():
    if len(wordpool) == 0:
        load_words()
    return (random.choice(wordpool) + random.choice(wordpool)).upper()

def draw_proper_noun():
    if len(namepool) == 0:
        load_words()
    return (random.choice(namepool)).upper()

def is_valid_name(w):
    return re.fullmatch(VALID_NAME_PATTERN, w)

def is_valid_word(w):
    return re.fullmatch(VALID_WORD_PATTERN, w)

def load_words():
    global namepool
    global wordpool
    with open(DICTFILE, 'r') as dictfile:
        words = dictfile.read().splitlines()
        namepool = list(filter(is_valid_name, words))
        wordpool = list(filter(is_valid_word, words))


if __name__ == '__main__':
    print(draw())
    print(draw_proper_noun())