import random
import pickle


def generate(model, length, seed=None):
    with open(model, 'rb') as f:
        dict_of_word = pickle.load(f)
    with open('answer.txt', 'w', encoding='utf-8') as f:
        if seed is None:
            ans = [random.choice(list(dict_of_word))]
        else:
            ans = [seed]
        for i in range(length):
            ans.append(random.choice(dict_of_word[ans[i - 1]]))
        s = ' '.join(ans)
        f.write(s)

