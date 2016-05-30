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
- XXX
- XXX
- XXX
"""

"""Section 5: XXX
- XXX
- XXX
- XXX
"""
