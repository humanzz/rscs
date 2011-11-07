import nltk
import nltk.data
from nltk.tokenize import *
sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
file = open('en.txt','r')
text = file.read()
sents = sent_tokenizer.tokenize(text)
print(sents[171:181])