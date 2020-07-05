"""
An example about how iterables and iterators works
"""

'''
below class is an example of iterables
'''
class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()


    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        index = self.index
        self.index += 1
        return self.words[index]

"""
An example for generator function
"""
def sentence(sentence):
    for word in sentence.split():
        yield word

# my_sentence = Sentence('this is a test')
my_sentence = sentence('this is a test')

for word in my_sentence:
    print(word)