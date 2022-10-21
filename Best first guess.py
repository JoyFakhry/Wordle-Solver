from big_list import valid_WORDS, answer_WORDS
from collections import Counter


def letter_frequencies(name):
    if name == 'valid':
        word_list = valid_WORDS
        print('All valid words')
    elif name == 'answers':
        word_list = answer_WORDS
        print("All answer words")

    num_letters = len(word_list[0])
    big_counter = Counter(word_list[0])
    for word in word_list[1::]:
        little_count = Counter(word)
        big_counter.update(little_count)
        num_letters += len(word)

    print("Letter | Frequency | Percent of all letters")
    for letter, freq in sorted(big_counter.items(), key=lambda item: item[1], reverse=True):
        print(f'{letter.center(6)} {str(freq).center(12)}  \t  {str(freq/num_letters*100).center(10):.5}%')


letter_frequencies('valid')
print()
# letter_frequencies('answers')