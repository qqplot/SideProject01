def split_words(value):
    words = value.split(' ')
    return words

def sort_words(words):
    return sorted(words)

def print_first_word(words):
    word = words.pop(0)
    print(word)

def print_last_word(words):
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = split_words(sentence)
    return sort_words(words)

def first_last_print(setence):
    words = split_words(setence)
    f_word = print_first_word(words)
    l_word = print_last_word(words)

def sort_first_last_print(sentence):
    words = sort_words(split_words(sentence))
    print_first_word(words)
    print_last_word(words)
