import re
from typing import List
from string import ascii_lowercase
from termcolor import colored

from utils.random_word import read_from_words, random_word
from utils.hangman_ascii import HANGMANPICS as pics

def guess_letter(used_letters:List[str]):
    while True:
        guess = str(input("Enter guess: ")).lower()
        if guess.isalpha() and len(guess) == 1:
            if guess in used_letters:
                print("This guess was already made!")
                continue
            break
        else:
            print("Invalid option, try again: ")

    return guess

def reveal_letters(guess, word, answer):
    if guess in word and "_" in answer:
        # searches the indecies of guessed letter in word.
        indecies = [l.start() for l in re.finditer(guess, word)] 
        # replaces _ with the guessed letter in every occurance.
        for idx in indecies:
            answer = answer[:idx] + guess + answer[idx + 1:]

    return answer



def hangman():
    words = read_from_words() # create a list of words.
    word = random_word(words) # pick a random word.

    used_letters = []
    remaining_letters = list(ascii_lowercase)

    MAX_GUESSES = 6
    guesses_count = 0
    answer = "_" * len(word)
    print(answer, "word size: ", len(word), "\n")

    while guesses_count < MAX_GUESSES:
        if "_" not in answer:
            break

        guess = guess_letter(used_letters)

        # pops the guessed letter from remaining options and appends it to used letters
        if guess not in used_letters:
            used_letters.append(remaining_letters.pop(remaining_letters.index(guess)))
            print("Used letters: " + ",".join(used_letters))
        print("Remaining letters: " + ",".join(remaining_letters))

        if guess in word:
            answer = reveal_letters(guess, word, answer)
            print(answer)
        elif guesses_count < MAX_GUESSES:
            print(pics[guesses_count])
            guesses_count += 1
        else:
            print(pics[guesses_count])
            break

    if "_" not in answer:
        print(colored("Congratulations, you have guessed the word!","yellow"))
    else:
        print(colored("You have failed","red"))
