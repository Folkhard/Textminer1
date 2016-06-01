# -*- coding: utf-8 -*-
"""
Created on Wed May 25 07:04:32 2016

@author: foucard

Object: large texts mining
Disclaimer below

"""


"""
Section 1: packages importation
"""

import nltk
from nltk.tokenize import TreebankWordTokenizer
from  nltk.corpus import stopwords
import re
import matplotlib.pyplot as plt
from matplotlib import pylab
import numpy


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

tokenizer = TreebankWordTokenizer()
textalpha= re.sub("[^a-zA-Z|\s]+","",text).lower()
words=tokenizer.tokenize(textalpha)
numberwords=len(words)

basicstopwords = stopwords.words('english')
addstopwords = ['the','us','thy','thou','ye','yet','also','unto','thee','therefore','still']
stopwords = [stopword.lower() for stopword in basicstopwords]+addstopwords
cleanwords = [w for w in words if w not in stopwords]
uniquewords = list(set(cleanwords))
numberuniquewords=len(uniquewords)

"""Section 3: working on words frequency
- Counting 
- Plotting top 25 words
- Plotting distribution of top 10 words
- XXX
"""

wordcounts = nltk.FreqDist(cleanwords)

def topwords(wordcounts, N):
    output=[(k,v) for k,v in wordcounts.items()]
    output.sort(key=lambda x: x[1], reverse=True)
    return output[:N]
    
def bar_plot(wordlist, N, title="Occurence count"):
    x=numpy.arange(1,N+1)

    ycountlist=[v for k,v in wordlist]
    labels=[k for k,v in wordlist]
    plt.bar(x-1, ycountlist, width=1, color=(0.2588,0.4433,1.0))
    plt.xlabel('Words in text')
    plt.xticks(x-0.5, labels, rotation=-90, size=8)
    pylab.title(title)
    plt.ylabel('# of occurences')
    plt.show()

bar_plot(topwords(wordcounts,25),25)

def dispersion_plot(words, w, title="Lexical Dispersion Plot"):
    w.reverse()
    w = list(map(str.lower, w))
    
    points = [(x,y) for x in range(len(words))
                    for y in range(len(w))
                    if words[x] == w[y]]
    if points:
        x, y = list(zip(*points))
    else:
        x = y = ()
    pylab.plot(x, y, "b|", scalex=.1)
    pylab.yticks(list(range(len(w))), w, color="k")
    pylab.ylim(-1, len(w))
    pylab.title(title)
    pylab.xlabel("Word Offset")
    pylab.show()

dispersion_plot(words,[k for k,v in topwords(wordcounts,25)])

"""Section 4: looking for specific words
- As per section 3 but with words list input on request
"""
def trywords():
    wordlist = input("Enter words searched (split by ', '):")
    wordlist=wordlist.split(", ")
    dispersion_plot(words, wordlist)
    wordlist=[(w,textalpha.count(w)) for w in wordlist]
    bar_plot(wordlist,len(wordlist))

"""Section 5: text richness
- Average number of words per sentence
- Number of unique words vs. total number of words
- Number of unique words needed to reach 80% of text
- XXX
"""

"""Section 6: looking for frequent sentences / part of sentences
- Cut text in lists of sentences (moving window) of 3, 4, 5,... words
- Weight sentences according to more frequent words and frequency of sentence
- XXX
"""

"""Section 7: name, adjective, verb filters on words lists or dictionaries
- XXX
"""

"""Section 8: cut text in chapters
- find double \n, "***", "---", etc.
- XXX
"""

"""Section 9: sentiment analysis
- XXX
"""

"""Section 10: text format converter in txt (in other script, called here?)
- XXX
"""

"""Disclaimer
Copyright (C) 2001-2016 NLTK Project
    Author: Steven Bird <stevenbird1@gmail.com>
    URL: <http://nltk.org/>
    License information, see LICENSE.TXT
Copyright (C) Matlplotlib
Copyright (C) Numpy
Copyright (C) Re
"""
