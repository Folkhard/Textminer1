# Textminer1
#YM-CF Textminer repository. Project to be defined

# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

"""
Script analyse de texte

Charles Foucard 03.05.2016
"""
            
import re
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


'''Open text to analyze'''

filename = input("Enter a filename: ")

with open(filename) as f:
    text = f.read()

'''Transform text in dictionary with # of occurences'''

words = re.findall(r"\w+", text)

cap_words = [word.upper() for word in words]

word_counts = Counter(cap_words)

'''Transform dictionary to list'''

word_list1=word_counts.items()

'''Sort list from larger number of occurences to smaller'''

word_list1=sorted(word_list1, key=lambda I:I[1], reverse=True)

'''Remove from list words smaller than 3 characters'''

word_len1=len(word_list1)
i=0
word_list2= []

while i < word_len1:
    if len(word_list1[i][0]) >= 3:
        word_list2.append(word_list1[i])
    i+=1

'''Remove from list unuseful words'''

word_len2=len(word_list2)
i=0
word_list3 = []

while i < word_len2:
    if word_list2[i][0] not in ('LES','QUI','EST','QUE','DES','PAS','UNE','TES','FIT','LUI','EUX','SUR','ONT','DIT','SON','PAR','AUX','DIS','TON','VOS','TOI','CAR','MON','ÉTÉ','MOI','NOS','SES','FUT','CES','MES','NOUS','VOUS','POUR','CEUX','DANS','COMME','LEUR','SONT','AVONS','LEURS','FAIT','DONC','ALORS','MAIS','TOUT','QUAND','CERTES','AVEC','PUIS','VOTRE','CELUI','ENTRE','PLUS','AINSI','PARMI','VERS','SERA','VOILÀ','ELLE','IL','ILS','ELLES','CELA','SERONT','SEREZ','TRÈS','CONTRE','AFIN','QUICONQUE','DEUX','NOTRE','MÊME','DIRENT','AVEZ','PART','APRÈS','AVANT','ÊTRE','SANS','TOUS','AUTRES','DISENT','VRAIMENT','AUPRÈS','AUTRE','RIEN','AURONT','JAMAIS','AVAIT','AURA','ÉTAIT','DONT','TOUTE','VEUT','ÊTES','ENSUITE','SUIS','MÊMES','ÉTAIENT','FAIRE','JUSQU','AUCUN','DEHORS','SOIT','FAITES','LORSQU','PEUT','FONT','CEPENDANT','LORSQUE','POINT','DESCENDRE','DONNÉ','AUCUNE','DELÀ','CERTAINEMENT','CHOSE','AUSSI','CETTE','PARCE','AYANT','DEVANT','VOICI','SELON','ENCORE','TOUTES','ÉTANT','DISANT','TROIS','MILLE','AVAIENT','PENDANT','SOUS','SEPT','MAINTENANT','CETTE','PARCE','AYANT','DEVANT','SELON','ENCORE','TOUTES','DISANT','CAUSE','QUELQU','FURENT'):
        word_list3.append(word_list2[i])
    i+=1
    
'''Select only top 25 occurences'''

i=0
word_list4 = []

while i < 25:
        word_list4.append(word_list3[i])
        i+=1

'''Output data'''

print(word_list4)

N=len(word_list4)
x=np.arange(1,N+1)

ycountlist=[b for (a, b) in word_list4]
labels=[a for (a, b) in word_list4]
plt.bar(x-1, ycountlist, width=1, color=(0.2588,0.4433,1.0))
plt.xlabel('Words in text')
plt.xticks(x-0.5, labels, rotation=-90, size=8)
plt.ylabel('# of occurences')
plt.title('Text analysis result')
plt.show()
        
