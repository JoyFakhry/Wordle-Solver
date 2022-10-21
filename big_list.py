filename = "valid-wordle-words.txt"
with open(filename, 'r') as f:
    valid_WORDS = f.read().splitlines()

filename = "in_order.txt"
with open(filename, 'r') as f:
    answer_WORDS = f.read().splitlines()

alpha = 'abcdefghijklmnopqrstuvwxyz'
filename = "Word_frequency.txt"
with open(filename, 'r', encoding="utf-8") as f:
    frequency_WORDS = {}
    for line in f.read().splitlines():
        line = line.split()

        flag = True
        for letter in line[0]:
            if letter not in alpha:
                flag = False
        if flag:
            frequency_WORDS[line[0]] = int(line[2])
