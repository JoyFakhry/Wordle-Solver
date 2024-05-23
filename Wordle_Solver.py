import random
import string
# cached list of all valid words and dict of frequency of words
from big_list import valid_WORDS, frequency_WORDS
from termcolor import colored   # pip install termcolor to work


# import sys
# import subprocess
# subprocess.check_call([sys.executable, '-m', 'pip', 'install',
#    'termcolor'])


# function to check if a word in word list matches user guess
# returns true if it can be used, false otherwise
def check_guess(guess):
    for index, letter in enumerate(u_tiles):    # check grey tiles first
        if (letter in g_tiles) or (letter in y_tiles):  # if letter occurs twice in guess
            if guess[index] == letter:  # if letter is in the same position as guessed word
                u_letters.add(letter)  # add letter to set of unused tiles
                return False
        elif (letter != '') and (letter in guess):  # if letter is in guessed word and occurs once
            u_letters.add(letter)
            return False
    for index, letter in enumerate(g_tiles):    # check green tiles next
        # if green tile not in same position as word
        if (letter != '') and (guess[index] != letter):
            return False
    keep = [True]   # initialize list for each letter in yellow tiles
    for index, letter in enumerate(y_tiles):
        if (letter in u_tiles) or (letter in g_tiles):  # if letter occurs twice in guess
            if guess.count(letter) < 2:  # if letter occurs once in guess
                return False
        if (letter != '') and (letter not in guess):    # if letter not in word
            return False
        elif (letter != '') and (letter in guess):  # if letter in word
            keep.append(guess[index] != letter)     # temporarily keep the word
    return all(keep)    # only return true if all yellow tiles match with word


# function to return random word from a word list
def random_guess(word_list):
    a_word = random.choice(word_list)
    if len(word_list) > 20:     # if there are a lot of possible words
        # loop through word until you don't get repeating letters
        while len(a_word) != len(set(a_word)):
            a_word = random.choice(word_list)   # get random choice from list
    return a_word


def frequency_guess(word_list):
    best_word_score = 0
    best_word = ''
    for word in word_list:
        if (word in frequency_WORDS) and (frequency_WORDS[word] > best_word_score):
            best_word = word
            best_word_score = frequency_WORDS[word]
    return best_word


# function to enumerate lists of history of possible guesses from previous rounds
def possible_guesses(list_of_lengths):
    print("\nPossibilities History:")
    for index, length in enumerate(list_of_lengths):
        print(f"Guess {index}: {length}")


def letters_used():
    sorted_set = sorted(u_letters)
    print(
        f"Grayed out letters (don't guess words with these {len(sorted_set)} letters): {''.join(sorted_set)}")


if __name__ == "__main__":

    print("Wordle Solver\n")

    print('Random first guess:', colored(
        f'{random_guess(valid_WORDS).upper()}', 'red'))
    previous_possibilities = valid_WORDS    # initialize to whole valid word list
    # initialize to length of whole valid word list
    len_of_possibilities = [len(valid_WORDS)]

    u_letters = set()  # initialize to empty set of grey letters
    guess_number = 1    # guess number counter initialization
    while len_of_possibilities[-1] != 1:    # loop until only one guess is left
        possibilities = []  # initialize list of possible words to guess next
        print('-'*10)
        print(f'Guess {guess_number}')

        # initialize lists for each tile type for this round
        u_tiles = []
        g_tiles = []
        y_tiles = []

        # get user input
        print("Enter " + colored("green ", "green") +
              "letters (return/enter for empty)")
        g_tiles.append(input(colored('Green 1: ', 'green')))
        g_tiles.append(input(colored('Green 2: ', 'green')))
        g_tiles.append(input(colored('Green 3: ', 'green')))
        g_tiles.append(input(colored('Green 4: ', 'green')))
        g_tiles.append(input(colored('Green 5: ', 'green')))

        print("Enter " + colored("yellow ", "yellow") +
              "letters (return/enter for empty)")
        y_tiles.append(input(colored('Yellow 1: ', 'yellow')))
        y_tiles.append(input(colored('Yellow 2: ', 'yellow')))
        y_tiles.append(input(colored('Yellow 3: ', 'yellow')))
        y_tiles.append(input(colored('Yellow 4: ', 'yellow')))
        y_tiles.append(input(colored('Yellow 5: ', 'yellow')))

        print("Enter " + colored("gray ", "grey") +
              "letters (return/enter for empty)")
        u_tiles.append(input(colored('Gray 1: ', 'grey')))
        u_tiles.append(input(colored('Gray 2: ', 'grey')))
        u_tiles.append(input(colored('Gray 3: ', 'grey')))
        u_tiles.append(input(colored('Gray 4: ', 'grey')))
        u_tiles.append(input(colored('Gray 5: ', 'grey')))

        # get list of possible words that match current guess and possible words
        possibilities = list(filter(check_guess, previous_possibilities))
        len_of_possibilities.append(len(possibilities))
        possible_guesses(len_of_possibilities)  # print possibilities history
        letters_used()  # print grey letters found so far
        next_guess = frequency_guess(possibilities)
        print("Next guess:", colored(next_guess.upper(), attrs=["bold"]))

        # if there are only a few choices remaining, print all of them
        if (len(possibilities)) <= 6 and (len(possibilities) != 1):
            print('\nRemaining choices:')
            for word in possibilities:
                if word == next_guess:
                    continue
                else:
                    print(word.upper())
        # set next rounds word list to this rounds solutions
        previous_possibilities = possibilities
        if len_of_possibilities[-1] != 1:
            guess_number += 1   # increment guess counter when there needs to be another guess


print(f"\nCongrats, this game took {guess_number} guesses")
