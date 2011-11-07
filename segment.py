import nltk
import nltk.data
from nltk.tokenize import *

sent_tokenizer=nltk.data.load('tokenizers/punkt/english.pickle')
file = open('smallEn.txt','r')
text = file.read()
words = nltk.word_tokenize(text)
PosTags = nltk.pos_tag(words)

def f(x): 
	[a1,a2] = x
	return a2 == 'JJ' or a2 == 'JJR' or a2 == 'JJS' or a2 == 'RB' or a2 == 'RBR' or a2 == 'RBS'

filtPosT = filter(f, PosTags)
def unfold(x):
	[a1,a2] = x
	return a1

wordlist = map(unfold,filtPosT)
print(wordlist)
