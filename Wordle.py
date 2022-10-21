from collections import defaultdict
import random
import string
from big_list import valid_WORDS

try:
    from termcolor import colored  # pip install termcolor to work
    flag = 1
except: # incase termcolor isn't installed, print normally
    flag = 0


random_guess = random.choice(valid_WORDS)
print('Random first guess:', random_guess)


# Obtain user input for letters and type
# Enter Green Tiles (empty default)
print("Enter green letters (return/enter for empty)")
g_tile_1 = input('Green 1: ')
g_tile_2 = input('Green 2: ')
g_tile_3 = input('Green 3: ')
g_tile_4 = input('Green 4: ')
g_tile_5 = input('Green 5: ')

g_tiles = [g_tile_1, g_tile_2, g_tile_3, g_tile_4, g_tile_5]
for index, value in enumerate(g_tiles): # Replace empty tiles with space to make output look nicer
    if value =='':
        g_tiles[index] = ' '


# Enter Yellow Tiles (space default)
print("Enter yellow letters (return/enter for empty)")
y_tile_1 = input('Yellow 1: ')
y_tile_2 = input('Yellow 2: ')
y_tile_3 = input('Yellow 3: ')
y_tile_4 = input('Yellow 4: ')
y_tile_5 = input('Yellow 5: ')

y_tiles = [y_tile_1, y_tile_2, y_tile_3, y_tile_4, y_tile_5]
for index, value in enumerate(y_tiles): 
    if value =='':
        y_tiles[index] = ' '

b_tiles = list(input('Enter grayed out letters (enter/return to skip or continue): ')) # Separate characters into list to iterate through

# Take intersection of all possibilities sets to only keep words similar to all sets
def find_Possibilities(possibilities):
    keys = [*possibilities]
    if len(keys) == 1:
        output = possibilities[keys[0]]
    elif len(keys) == 2:
        output = possibilities[keys[0]].intersection(possibilities[keys[1]])
    elif len(keys) == 3:
        output = possibilities[keys[0]].intersection(possibilities[keys[1]], possibilities[keys[2]])
    elif len(keys) == 4:
        output = possibilities[keys[0]].intersection(possibilities[keys[1]], possibilities[keys[2]], possibilities[keys[3]])
    elif len(keys) == 5:
        output = possibilities[keys[0]].intersection(possibilities[keys[1]], possibilities[keys[2]], possibilities[keys[3]], possibilities[keys[4]])
    else:
        return set()
    return output

def random_output():
    if rand == 'y':
        print(colored(f'Random answer from {len(output)} possible answers:', attrs=['underline']))
        print(str(output.pop()).upper())
        if len(output) <= 6:
            print('\nRemaining choices:')
            for word in output:
                print(word.upper())
    else:
        print(colored(f'{len(output)} Valid Answers:', attrs=['underline']))
        for word in sorted(output):
            print(word.upper())

which_words = input('Show possible answers (enter) or all valid words (y): ')
if which_words == 'y':
    from big_list import valid_WORDS
    WORDS = valid_WORDS
else:
    from big_list import answer_WORDS
    WORDS = answer_WORDS

rand = input('Output single, randomly chosen word from possible answers (y): ')

g_possibilities = defaultdict(set) # Initialize dictionary of empty sets
y_possibilities = defaultdict(set)

for word in WORDS: # LOOP through full word-list
    for index, letter in enumerate(g_tiles): # LOOP through green letters
        if word[index] == letter: # If letter is in the word at the correct spot
            g_possibilities[index].add(word) # Add that word as a green possibility by adding it to the dictionary, organized by letter index

    for index, letter in enumerate(y_tiles):  # LOOP through yellow letters
        if (letter in word) and (word[index] != letter): # If letter is in the word and not in the same spot
            y_possibilities[index].add(word) # Add that word as a yellow possibility

g_Possibilities = find_Possibilities(g_possibilities) # Sift all green possibilities to remove repeats
y_Possibilities = find_Possibilities(y_possibilities) # Sift all green possibilities to remove repeats

# Removes empty sets
if not bool(g_Possibilities):
    Possibilities = y_Possibilities
elif not bool(y_Possibilities):
    Possibilities = g_Possibilities
else:
    Possibilities = g_Possibilities.intersection(y_Possibilities)

if len(Possibilities) == 0: # If no green and yellow tiles, possibilities at this stage are all words
    Possibilities = WORDS


# Remove words that have letters in the bad tiles list
output = set()
for word in Possibilities:
    ok = True
    for letter in b_tiles:
        if letter in word:
            ok = False
    if ok:
        output.add(word)

# Print the results
g = "|" + "|".join(g_tiles) + "|"
y = "|" + "|".join(y_tiles) + "|"
b = "|" + "|".join(b_tiles) + "|"
if flag:
    print(colored("\nInput", attrs=['underline']))
    print(colored(g, 'green', attrs=['bold']), '(letters in the word and in the correct spot)')
    print(colored(y, 'yellow', attrs=['bold']), '(letters in the word but in the wrong spot)')
    print(colored(b, 'grey', attrs=['bold']), '(letters not in the word)\n')

    if (len(output) == 0) and (len(g_tiles) != 5) or (len(output) == 0) and (len(y_tiles) != 5):
        print('why')
        print(len(g_tiles), len(y_tiles))
        print("No possible solutions")
    elif (len(output) == 0) and (len(b_tiles) >=5) and (len(g_tiles) == 5) and (len(y_tiles) == 5):
        for word in WORDS:
            ok = True
            for letter in b_tiles:
                if letter in word:
                    ok = False
            if ok:
                output.add(word)
        random_output()
    else:
        if which_words == 'y':
            random_output()
        else:
            print(colored(f'{len(output)} Possible Answers (and (roughly) the day the word occurred or will occur):', attrs=['underline']))
            for word in sorted(output):
                print(word.upper(), WORDS.index(word))
else:
    print("\nInput")
    print('Green letters: ', g, '(letters in the word and in the correct spot)')
    print('Yellow letters:', y, '(letters in the word but in the wrong spot)\n')
    if len(output) == 0:
        print('huh')
        print("No possible solutions")
    else:
        print(f'{len(output)} Possible Answers (and (roughly) the day the word occurred or will occur):')
        for word in sorted(output):
            print(word.upper(), WORDS.index(word))



