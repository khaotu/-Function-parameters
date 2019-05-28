import random

def hello(word,array_data):
    get_indexes = lambda find_word, data: [i for (y, i) in zip(data, range(len(data))) if find_word == y]
    index = get_indexes(word,array_data)
    if(index==[]):
        return "not found"
    else:
        return "this word found in index : " + str(random.choice(index))
