#!/usr/bin/env python
# Terminal Wordle

word = "python" # temporary word
guessed = []

def check_guess(guess):
    ## FIX THIS ##
    if not guess.isalpha():
        print("Invalid characters, try again")
        ## Should break & not count as a try

        if len(guess) > 6:
            print("\033[91mToo many letters")
            print("\033[0m") # resets text formatting/styling
        elif len(guess) < 6:
            print("\033[91mToo few letters")
            print("\033[0m") # resets text formatting/styling
    else:
        return True

def check_word(guess):
    split_word = list(word)
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
    guessed.append(''.join(temp_guess))

def display_results(guesses):
    print(f"Guesses left: {guesses}")
    print("Past guesses:")
    if guessed != []:
        for i in guessed:
            print(i)
    print("\033[0m") # resets text formatting/styling

def main():
    print("\nTerminal Wordle!\nGuess the 6 letter word, in 6 tries!\n")
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

        if guesses == 0:
            print("No more guesses left...")
            print("\033[91mYOU LOSE!")
            won = True

        if guess.lower() == word.lower():
            print(f"Correct! The word was {word}!")
            print("\033[92mYOU WIN!")
            won = True


main()
