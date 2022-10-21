from cProfile import label
from big_list import valid_WORDS, answer_WORDS
from collections import Counter, defaultdict
from matplotlib import pyplot as plt
 
 
def find_dup_char(input):
 
    # now create dictionary using counter method
    # which will have strings as key and their
    # frequencies as value
    WC = Counter(input)
 
    # Finding no. of  occurrence of a character
    # and get the index of it.
    output = {}
    for letter, count in WC.items():
        if (count > 1):
            output[letter] = count

    return output
 
doubles_valid = defaultdict(int)  
triples_valid = defaultdict(int)  
for word in valid_WORDS:
    dic = find_dup_char(word)
    if dic != {}:
        for letter in dic:
            if dic[letter] == 2:
                doubles_valid[letter] += 1
            elif dic[letter] == 3:
                triples_valid[letter] += 1
            else:
                print(word, dic)

doubles_answer = defaultdict(int)  
triples_answer = defaultdict(int)  
for word in answer_WORDS:
    dic = find_dup_char(word)
    if dic != {}:
        for letter in dic:
            if dic[letter] == 2:
                doubles_answer[letter] += 1
            elif dic[letter] == 3:
                triples_answer[letter] += 1
            else:
                print(word, dic)



def plot_data(doubles, triples, length, title):
    plt.figure(figsize=(12, 8), dpi=80)
    bar1 = plt.bar(*zip(*sorted(doubles.items(), key=lambda item: item[1], reverse=True)), label='Doubles')
    bar2 = plt.bar(*zip(*sorted(triples.items(), key=lambda item: item[1], reverse=True)), label='Triples')

    if title == 'valid words':
        height = 800
        bump = 10
    else:
        height = 150
        bump = 1
    plt.text('x', height, f'Number of {title}: {length}', size=15, ha='right')


    for rect in bar1+bar2:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2.0, height + bump, f"{100*height/length:.2f}%", ha='center', va='bottom', fontsize=10)

  

    plt.xlabel('Letters')
    plt.ylabel('Occurrences')
    plt.title(f'Wordle: Repeat letter occurrences in all {title}')
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'Pics/{title}')
    # plt.show()


plot_data(doubles_valid, triples_valid, len(valid_WORDS), 'valid words')
plot_data(doubles_answer, triples_answer, len(answer_WORDS), 'answers')