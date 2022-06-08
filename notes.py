# the problem yesterday with the BattleMage class inheritance was that the inheritance class order was not considered.
# the BattleMage class looked for __init__ in itself, and when it found that, it overrode the __init__ method from the parent class.
# __init__ is called whenever a class definition is called to create a new object


# open a file
file = open("sample2.txt")

sentenceList = file.readlines()

#ASSIGNMENT:
'''
Open a text file.


Read in all of its text (one chunk at a time)
Split each chunk of text into sentences by the "." character.
Measure the length of each sentence.
Count the number of sentences whose length you have measured.
Sum the sentence lengths and divide that by the number of sentences.

'''

file = open("sample2.txt", encoding="utf=8")

chunkList = file.readlines()

numberOfSentences = 0
length = 0

for chunk in chunkList:
        sentences = chunk.split(".")
        for i in sentences:
            numberOfSentences = numberOfSentences + 1
            length = length + len(i.split())

result = length/numberOfSentences


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