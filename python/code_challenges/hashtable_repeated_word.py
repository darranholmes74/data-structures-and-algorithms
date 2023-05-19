from data_structures.hashtable import Hashtable
import string


def first_repeated_word(key):
    ht = Hashtable()
    for word in key.lower().split():
        word = word.translate(str.maketrans("", "", string.punctuation))
        if ht.has(word):
            return word
        else:
            ht.set(word, None)
    return None
