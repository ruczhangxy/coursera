from random import randint
from dictutil import *
from functools import reduce

## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    review_options = ["See it!", "A gem!", "Ideological claptrap!"]
    return review_options[randint(0, len(review_options) - 1)]

## Tasks 2 and 3 are in dictutil.py

## Task 4    
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.

    Note that to test your function, you are welcome to use the files stories_small.txt
      or stories_big.txt included in the download.
    """
    ret_dict = {}
    for i, content in enumerate(strlist):
        #lines = content.split('\n')
        #print('Lines:', len(lines))
        #for line in content:
        words = content.strip().split(' ')
        for word in words:
            if word not in ret_dict:
                ret_dict[word] = set()
            ret_dict[word].add(i)
    return ret_dict

## Task 5
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    """
    ret_set = set()
    for word in query:
        doc_ids = inverseIndex.get(word,[])
        for doc_id in doc_ids:
            ret_set.add(doc_id)
    return ret_set

## Task 6
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    """
    doc_sets = [inverseIndex.get(word, set()) for word in query]
    ret_set = reduce(lambda a,b:a&b, doc_sets)
    return ret_set
