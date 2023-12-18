#!/usr/bin/env python3
# Terminal Wordle

from wordlist import word_choice

WORD = word_choice()
GUESSED = []

def check_guess(guess):
    if not guess.isalpha():
        print("\033[91mInvalid characters, try again")
        print("\033[0m") # resets text formatting/styling
    elif len(guess) > 5:
        print("\033[91mToo many letters")
        print("\033[0m") # resets text formatting/styling
    elif len(guess) < 5:
        print("\033[91mToo few letters")
        print("\033[0m") # resets text formatting/styling
    else:
        return True

def check_word(guess):
    split_word = list(WORD)
    split_guess = list(guess)
    temp_guess = [] 
    for i in split_guess:
        temp_i = f""
        if (i in split_word) and split_word.index(i) == split_guess.index(i):
            temp_i = f"\033[92m{i.upper()} " # green
            temp_guess.append(temp_i)
        elif i in split_word:
            temp_i = f"\033[93m{i.upper()} " # yellow
            temp_guess.append(temp_i)
        else:
            temp_i = f"\033[0m{i.upper()} " # white
            temp_guess.append(temp_i)
    GUESSED.append(''.join(temp_guess))

def display_results(guesses):
    print(f"Guesses left: {guesses}")
    print("Past guesses:")
    if GUESSED != []:
        for i in GUESSED:
            print(i)
    print("\033[0m") # resets text formatting/styling

def main():
    print("\nTerminal Wordle!\nGuess the 5 letter word, in 6 tries!\n")
    print("\033[93mLetters in Yellow are correct, BUT in the wrong place")
    print("\033[92mLetters in Green are correct, AND in the correct place")
    print("\033[0m") # resets text formatting/styling
    won = False
    guesses = 6

    while not won:
        guess = input("Your Guess?\n")
        if check_guess(guess):
            guesses -= 1
            check_word(guess)

        display_results(guesses)

        if (guesses == 0) and (guess.lower() != WORD.lower()):
            print("No more guesses left...")
            print(f"The word was {WORD}!")
            print("\033[91mYOU LOSE!")
            print("\033[0m") # resets text formatting/styling
            won = True

        if guess.lower() == WORD.lower():
            print(f"Correct! The word was {WORD}!")
            print("\033[92mYOU WIN!")
            print("\033[0m") # resets text formatting/styling
            won = True


main()
