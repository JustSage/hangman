import random
from typing import List

def read_from_words() -> List[str]:
    with open("utils/words.txt", "r") as file:
        words = file.read().splitlines()
        words.sort()
    return words

def random_word(words: List[str]) -> str:
    return words[random.randint(0,len(words))]
