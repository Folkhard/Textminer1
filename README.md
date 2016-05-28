# -*- coding: utf-8 -*-
"""
Created on Wed May 25 07:04:32 2016

@author: foucard

Object: large texts mining

"""


"""
Section 1: packages importation
"""

import nltk
from nltk.tokenize import TreebankWordTokenizer
from  nltk.corpus import stopwords
from collections import Counter
import re
#import matplotlib
#import numpy


"""
Section 2: loading the text and preparing it
- Ask for text to open (for the moment limited to .txt in same directory)
- Open text
- Read text
- Tokenize text
- Cut text in sentences
- Count number of sentences
- Clean non alphabetical signs
- Lowercase words
- Count number of words
- Clean stopwords
- Cut text in unique words
- Count number of unique words
"""

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()
    
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentences=tokenizer.tokenize(text)
numbersentences=len(sentences)
#print(sentences)
#print(numbersentences)

tokenizer = TreebankWordTokenizer()
textalpha= re.sub("[^a-zA-Z|\s]+","",text)
words=tokenizer.tokenize(textalpha)
words = [word.lower() for word in words]
numberwords=len(words)
#print(words)
#print(numberwords)

basicstopwords = stopwords.words('english')
addstopwords = ['the','us','thy','thou','ye','yet','also','unto','thee']
stopwords = [stopword.lower() for stopword in basicstopwords]+addstopwords
cleanwords = [w for w in words if w not in stopwords]
uniquewords = list(set(cleanwords))
numberuniquewords=len(uniquewords)
#print(stopwords)
#print(cleanwords)

"""Section 3: working on unique words frequency
- Counting 
- Plotting top 50 words
- Plotting distribution of top 10 words
- XXX
"""

wordcounts = Counter(cleanwords)
#print(wordcounts)

"""Section 4: looking for specific words
- XXX
- XXX
- XXX
"""

"""Section 5: XXX
- XXX
- XXX
- XXX
"""
