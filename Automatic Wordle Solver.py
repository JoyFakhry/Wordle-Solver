from turtle import tiltangle
from big_list import answer_WORDS, valid_WORDS, frequency_WORDS
import random

answer_WORDS_offset = 23 # Add 23 to answer_words index to get actual current day


def color_tiles(answer, guess):
    tiles = {'yellow': ['', '', '', '', ''], \
        'green': ['', '', '', '', ''], \
        'grey': ['', '', '', '', '']}

    for index, letter in enumerate(guess):
        if letter in answer and guess[index] == answer[index]:
            tiles['green'][index] = letter
    for index, letter in enumerate(guess):
        if letter in answer and guess[index] != answer[index]:
            if letter not in tiles['green']:
                tiles['yellow'][index] = letter
    for index, letter in enumerate(guess):
        if letter not in answer:
            tiles['grey'][index] = letter
        else:
            if letter in tiles['green'] and guess[index] != answer[index]:
                tiles['grey'][index] = letter
    return tiles


def check_guess(guess):
    global tiles
    for index, letter in enumerate(tiles['grey']):    # check grey tiles first
        if (letter in tiles['green']) or (letter in tiles['yellow']):  # if letter occurs twice in guess
            if guess[index] == letter:  # if letter is in the same position as guessed word
                return False
        elif (letter != '') and (letter in guess):  # if letter is in guessed word and occurs once
            return False
    for index, letter in enumerate(tiles['green']):    # check green tiles next
        if (letter != '') and (guess[index] != letter): # if green tile not in same position as word
            return False
    keep = [True]   # initialize list for each letter in yellow tiles
    for index, letter in enumerate(tiles['yellow']):
        if (letter in tiles['grey']) or (letter in tiles['green']):  # if letter occurs twice in guess
            if guess.count(letter) < 2: # if letter occurs once in guess
                return False
        if (letter != '') and (letter not in guess):    # if letter not in word
            return False
        elif (letter != '') and (letter in guess):  # if letter in word
            keep.append(guess[index] != letter)     # temporarily keep the word
    return all(keep)    # only return true if all yellow tiles match with word


def random_guess(word_list):
    a_word = random.choice(word_list)
    if len(word_list) > 20:     # if there are a lot of possible words
        while len(a_word) != len(set(a_word)):  # loop through word until you don't get repeating letters
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


def solver(day, start, display):
    global tiles
    ANSWER = answer_WORDS[day + answer_WORDS_offset]
    if display:
        print(f"Today is day {day} and the word is {ANSWER.upper()}")
    previous_possibilities = valid_WORDS

    if start == 'random':
        guess = random_guess(valid_WORDS)
    elif start == 'orate':
        guess = 'orate'
    else:
        guess = start
    guess_number = 1

    while guess_number <= 6:
        if display:
            print(f"Guess {guess_number}: {guess.upper()}")
        if guess == ANSWER:
            if display:
                print(f'Congrats, you won in {guess_number} guesses!')
            return guess_number
        elif guess_number == 6:
            if display:
                print(f'Oof, you lost')
            return 'X'

        possibilities = []

        tiles = color_tiles(ANSWER, guess)
        possibilities = list(filter(check_guess, previous_possibilities))

        guess = frequency_guess(possibilities)
        previous_possibilities = possibilities
        guess_number += 1


if __name__ == "__main__":
    print('Automatic Wordle Solver')
    print('Input a day (0-2292) and starting word, and I will output the number of tries to get that')
    print()
    scores = []
    current_day = 489
    scores.append(solver(current_day, 'random', True))
    print()
    scores.append(solver(current_day, 'orate', True))


    print("Scores for Random and ORATE:")
    print(*scores, sep=", ")
