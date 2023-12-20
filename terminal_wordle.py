#!/usr/bin/env python3
# Terminal Wordle

from wordlist import word_choice
WORD = word_choice()
GUESSED = []

# Function to validate 'guess' input
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

# Function to check 'guess' against 'word'
def check_word(guess):
    split_word = list(WORD)
    split_guess = list(guess)
    temp_guess = [] 
    i = 0
    temp_i = f""

    # OLD FOR LOOP STRUCTURE:
    #for i in split_guess:
        #if (i in split_word) and split_word.index(i) == split_guess.index(i):
    ########################

    ### CHANGED ###
        # for loop iterating over list elements changed to
        # while loop iterating over index values
        #
        # this allows for a more accurate comparison of lists
        # since `.index()` only returns the first occurence of a value
    ###############

    while i < len(split_guess):
        # Correct letter & correct position
        if split_guess[i] == split_word[i]:
            temp_i = f"\033[92m{split_guess[i].upper()} " # green
            temp_guess.append(temp_i)
            i += 1
        # Just correct letter
        elif split_guess[i] in split_word:
            temp_i = f"\033[93m{split_guess[i].upper()} " # yellow
            temp_guess.append(temp_i)
            i += 1
        # No match
        else:
            temp_i = f"\033[0m{split_guess[i].upper()} " # white
            temp_guess.append(temp_i)
            i += 1

    # joins 'temp_guess' list into a string & appends it to 'guessed' list
    GUESSED.append(''.join(temp_guess))

# Function to display game results
def display_results(guesses):
    print(f"Guesses left: {guesses}")
    print("Past guesses:")
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

        # Validates 'guess' before continuing
        if check_guess(guess):
            guesses -= 1
            check_word(guess)
        display_results(guesses)

        # Lose Condition Check
        if (guesses == 0) and (guess.lower() != WORD.lower()):
            print("No more guesses left...")
            print(f"The word was {WORD}!")
            print("\033[91mYOU LOSE!")
            print("\033[0m") # resets text formatting/styling
            won = True

        # Win Condition Check
        if guess.lower() == WORD.lower():
            print(f"Correct! The word was {WORD}!")
            print("\033[92mYOU WIN!")
            print("\033[0m") # resets text formatting/styling
            won = True


if __name__ == "__main__":
    main()
