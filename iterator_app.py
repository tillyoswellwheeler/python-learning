#-------------------------------------
# Python Coding Problem -- Iterator
#-------------------------------------

#-------------------------------------
# Model a Sentence Data type via a class


class Sentence:

    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0                          # Self.index is set to 0
        self.words = self.sentence.split()

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.words):        # Self.index is set to 0 so does not raise exception
            raise StopIteration
        index = self.index                      # Self. index is set to 0 so does not raise exception
        self.index += 1
        return self.words[index]

# my_sentence = Sentence('This is a test')
# #
# # for word in my_sentence: # Created an Iterator on the class which means that the variable linked to the class can be interated over.
# #     print(word)
#
# print(next(my_sentence)) #Also you can use next on the variable created from the class
# print(next(my_sentence))

#-------------------------------------
# Create a Generator

def sentence(sentence):
    for word in sentence.split():
        yield word

my_sentence = sentence('This is a test')
#
# for word in my_sentence: # Created an Iterator on the class which means that the variable linked to the class can be interated over.
#     print(word)

print(next(my_sentence)) #Also you can use next on the variable created from the class
print(next(my_sentence))