# Prender un dossier des documents textes et les tokenizer, normalizer, lemmatizer (après l'option), et joindre en juste un document.
'''To use: install necessary modules (pip install unicodata, pip install itertools, etc... see lines 17-23 below)
Set options, including input folder and output filename. Then run:
python3 prepare_corpus.py.

Takes a long time to do a large dossier of documents.'''


#OPTIONS:
#nom du dossier avec textes (dans la meme place que le script)
input_dossier = '../Input'
# le type des fichiers
extension = "txt"
# nom du dossier text qui contiendrea
output_file = "../Output/corpus.txt"
lemmas = True

import unicodedata
import os, glob
import codecs
import re
import itertools
import importlib.machinery
import types
if lemmas == True:
    print("Lemmatize option selected. Loading dictionary...")
    import frenchlexicon
    # make the entire dictionary lowercase
    tups = [[key.lower(), frenchlexicon.DICT[key].lower()] for key in frenchlexicon.DICT.keys()]
    for tup in tups:
        frenchlexicon.DICT[tup[0]] = tup[1]
    import abbreviations


def normalizer(lines):
    '''Take a list of sentences and make them lowercase.
    Remove punctuation. Fix unicode errors.'''
    lines = [x.lower() for x in lines]
    lines = [re.sub("[\—\-\.,;!\*»«\(\)]", "", x) for x in lines]
    lines = [unicodedata.normalize('NFKD', x) for x in lines]
    return(lines)

def expand_abbreviations(word):
    for abbreviation, expansion in abbreviations.DICT.items():
        word = word.replace(abbreviation, expansion)
    return word

def lire_dossier(path):
    '''load all files in a folder with the given extension'''
    corpus = []
    for textfile in glob.iglob(f"{path}/*.{extension}"):
        f = codecs.open(textfile, encoding="utf-8")
        try:
            lines = f.readlines()
        except UnicodeDecodeError:
            f = codecs.open(textfile, encoding="latin-1")
            lines = f.readlines()
        # replace all punctuation with whitespace.
        lines = [re.sub("titre: Electronic Enlightenment", " ", x) for x in lines]
        lines = [re.sub("date: ", " ", x) for x in lines]
        lines = [re.sub("[.;!\?]", "\n", x) for x in lines]
        lines = [re.sub("[,\]\[\(\)0-9]", " ", x, count = 10000) for x in lines]
        lines = normalizer(lines)
        document = split_lines(lines)
        if lemmas == True:
            document = [expand_abbreviations(x) for x in document]
            document = [lemmatize(x) for x in document]
        corpus.append(document)
    #corpus = list(itertools.chain.from_iterable(corpus))
    return(corpus)

def split_lines(lines):
    '''take a list of lines and turn it into a list of words.'''
    lines = [x for x in lines if len(x) > 1]
    words = [x.split(sep=" ") for x in lines]
    #[x.append("\n") for x in words]
    corpus = list(itertools.chain.from_iterable(words))
    # remove all 'words' that lack letter characters
    corpus = [x for x in corpus if re.search("[a-zA-Z\n]", x)]
    return(corpus)

def imprimer(corpus, path):
    f = codecs.open(path, mode = 'w', encoding="utf-8")
    for doc in corpus:
        f.write(" ".join(doc))
        f.write("\n")

def load_dictionary(filename, path):
    print('Loading lemmata. This may take a minute.')
    loader = importlib.machinery.SourceFileLoader(filename, path)
    module = types.ModuleType(loader.name)
    loader.exec_module(module)
    return module.DICTIONARY

def lemmatize(word):
    '''Pass each token through the lemmatization dictionary, twice.
    This must be done twice because the dictionary contains two-step transformations.
    If the token does not exist in the dictionary, leave it as-is.'''
    if word in frenchlexicon.DICT.keys():
        word = frenchlexicon.DICT[word]
        if word in frenchlexicon.DICT.keys():
            return frenchlexicon.DICT[word]
        else:
            return word
    else:
        return word

if __name__ == "__main__":
    print ('Processing texts...')
    corpus = lire_dossier(input_dossier)
    print(len(corpus), "texts processed")
    print ('Printing output')
    imprimer(corpus, output_file)
