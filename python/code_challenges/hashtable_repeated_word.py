import string

from data_structures.hashtable import Hashtable


def first_repeated_word(key):
    ht = Hashtable()
    for word in key.lower().split():
        word = word.translate(str.maketrans("", "", string.punctuation))
        if ht.has(word):
            return word
        else:
            ht.set(word, None)
    return None
