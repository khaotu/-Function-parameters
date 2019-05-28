import random

list_fruit =["apple",
"apricot",
"avocado",
"banana",
"berry",
"apple",
"apricot",
"avocado",
"banana",
"berry",
"cantaloupe",
"cherry",
"citron",
"citrus",
"coconut",
"date",
"fig",
"apple",
"apricot",
"avocado",
"grape",
"guava",
"kiwi",
"lemon",
"lime",
"mango",
"melon",
"mulberry",
"nectarine",
"orange",
"papaya",
"peach",
"pear",
"pineapple",
"plum",
"prune",
"raisin",
"raspberry",
"tangerine"]

def hello(word):
    get_indexes = lambda find_word, data: [i for (y, i) in zip(data, range(len(data))) if find_word == y]
    index = get_indexes(word,list_fruit)
    if(index==[]):
        return "not found"
    else:
        return "this word found in index : " + str(random.choice(index))
