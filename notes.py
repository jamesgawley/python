
class Warrior:
     def __init__(self, name, age):
             self.name = name
             self.age = age
             self.strength = 10




# the problem yesterday with the BattleMage class inheritance was that the inheritance class order was not considered.
# the BattleMage class looked for __init__ in itself, and when it found that, it overrode the __init__ method from the parent class.
# __init__ is called whenever a class definition is called to create a new object


# open a file
open()

# make a list of sentences


# make a dictionary of type/token counts


# OR: count word/sentence lengths


# perform a chi-squared test
# Take the corpora associated with two authors.
# Merge them into a single, larger corpus.
# Count the tokens for each of the words that can be found in this larger corpus.
# Select the n most common words in the larger corpus.


'''
Calculate how many tokens of these n most common words we would have expected to find in each of the two original corpora if they had come from the same author. This simply means dividing the number of tokens that we have observed in the combined corpus into two values, based on the relative sizes of the two authors’ contributions to the common corpus.
'''


'''
Calculate a chi-squared distance by summing, over the n most common words, the squares of the differences between the actual numbers of tokens found in each author’s corpus and the expected numbers, divided by the expected numbers.
'''