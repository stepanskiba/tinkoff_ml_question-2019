import random
import pickle
import re


def fit(model, input_dir='stdin'):
    if input_dir == 'stdin':
        in_str = input()
    else:
        with open(input_dir, 'r', encoding='utf-8') as file_in:
            in_str = file_in.read()
    dict_of_word = {}
    lst = list(map(lambda x: x.replace('\n', ' '), in_str.split('.')))
    for elem in lst:
        lst_of_words = list(
            map(lambda y: ''.join(filter(lambda x: re.fullmatch(r'[а-яё-]', x), y.lower())), elem.split()))
        filter_words = list(filter(lambda x: x != '', lst_of_words))
        for i in range(1, len(filter_words)):
            if filter_words[i - 1] in dict_of_word:
                dict_of_word[filter_words[i - 1]].append(filter_words[i])
            else:
                dict_of_word[filter_words[i - 1]] = [filter_words[i]]
        if len(filter_words) > 1:
            dict_of_word[filter_words[-1]] = [random.choice(filter_words[:-1:])]
    with open(model, 'wb') as file_out:
        pickle.dump(dict_of_word, file_out)
