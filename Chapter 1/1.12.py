# Create a program that types randomly until it accidentally types "methinks it is like a weasel"

import random

def generate():
    return "".join([random.choice("abcdefghijklmnopqrstuvwxyz ") for _ in range(len("methinks it is like a weasel"))])

def score(guess):
    return sum([1 for i, letter in enumerate(guess) if "methinks it is like a weasel"[i] == letter])

def main():
    i = 0
    while True:
        for _ in range(100000):
            guess = generate()
            guess_score = score(guess)
            if guess_score == len(guess):
                print(i, guess, guess_score)
                return
            i += 1
        print(i, guess, guess_score)

# I'm not going to wait for this to finish running so idk if it works
main()
