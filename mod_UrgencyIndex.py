import pandas as pd
import os, sys, getopt, cPickle, csv, sklearn
from nltk.corpus import stopwords
import re
import nltk
import numpy



STOP = set(stopwords.words('english'))
words =  pd.read_csv('./Data/U_Keyword_Dataset.txt', sep='/n' , quoting=csv.QUOTE_NONE, names=["Urgency_Keywords"])#csv comma seperated value
print (words)
words = words.values#to numpy 
words = words.tolist()#to list
sub_str = "look into at as soon as possible "
tokens = nltk.word_tokenize(sub_str)
tagged = nltk.pos_tag(tokens)
print (tagged)
#print (type(tagged))
#remove IN CC VBZ DT RB VBP VBZ tags
count = 0
with open("./Data/U_Keyword_Dataset.txt") as f:
	for index in range(len(sub_str)):
		for line in f:
			if sub_str[index] in line:
				count = count +1
			        break
d = float(count)/float(len(sub_str))
print (d)
	


		 


	





