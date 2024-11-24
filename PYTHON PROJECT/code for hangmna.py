# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 15:14:23 2024

@author: user
"""

import random

allwords = ["aerospace", "ayesha", "spain", "tomorrowxtogether"]

def chooseword():
    return random.choice(allwords)

def hangmandisplay(tries):
    stages = [
        """________
           |     |
           O     |
         / | \\   |
           |     |
          / \\    |
                 |
        _________|""",
        """________
           |     |
           O     |
         / | \\   |
           |     |
          /      |
                 |
        _________|""",
        """________
           |     |
           O     |
         / | \\   |
           |     |
                 |
                 |
        _________|""",
        """________
           |     |
           O     |
         / | \\   |
                 |
                 |
                 |
        _________|""",
        """________
           |     |
           O     |
         / |     |
                 |
                 |
                 |
        _________|""",
        """________
           |     |
           O     |
           |     |
                 |
                 |
                 |
        _________|""",
        """________
           |     |
           O     |
                 |
                 |
                 |
                 |
        _________|""",
        """________
           |     |
                 |
                 |
                 |
                 |
                 |
        _________|"""
    ]
    return stages[tries]

def hangman():
    word = chooseword().upper()
    wordletters = set(word)

    guessedletters = set()
    tries = 7

    print("welcome to hangman!")
    print(hangmandisplay(tries))
    print("_ " * len(word))

    while tries > 0 and wordletters:
        currentword = [letter if letter in guessedletters else "_" for letter in word]
        print("\ncurrent word:", " ".join(currentword))
        guess = input("Guess a letter: ").upper()
        if len(guess) != 1 or not guess.isalpha():
            print("please enter a single alphabet.")
            continue
        if guess in guessedletters:
            print(f"youve already guessed '{guess}'. try again.")
        elif guess in wordletters:
            print(f"good job! '{guess}' is in the word.")
            guessedletters.add(guess)
            wordletters.remove(guess)
        else:
            print(f"'{guess}' is not in the word. you lose a try.")
            guessedletters.add(guess)
            tries -= 1
        print(hangmandisplay(tries))

    if not wordletters:
        print(f"\ncongratulations! youve guessed the word: {word}")
    else:
        print(f"\ngame over!!! the word was: {word}")

hangman()
