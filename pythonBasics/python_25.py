def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words
    pass

def sort_words(words):
    """Sorts the words."""
    return sorted(words)
    pass

def print_first_words(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word
    pass

def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word
    pass

def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)
    pass
def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_words(words)
    print_last_word(words)
    pass

def print_first_and_last_sorted(sentence):
    words = sort_sentence(sentence)
    print_first_words(words)
    print_last_word(words)
    pass
