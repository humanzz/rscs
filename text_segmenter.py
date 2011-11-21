import os
import nltk
import string

class TextSegmenter:
  corpusRoot = os.getcwd() + "/corpus/"
  
  def __init__(self, filename):
    self.filename = filename # include directory path like "www.amazon.com/10t1.txt"
    self.filepath = self.corpusRoot + filename

      
  def process(self):
	file = open(self.filepath,'r')
	text = file.read()
	# pos-tag the sentences
	words = nltk.word_tokenize(text)
	posList = nltk.pos_tag(words)
	# list of all PosTag Tuples that we want to extract
	tagTuples = [('JJ','NN'),('JJ','NNS'),('RB','JJ'),('RBR','JJ'),('RBS','JJ'),('JJ','JJ'),('NN','JJ'),('NNS','JJ'),('RB','VB'),('RBR','VB'),('RBS','VB'),('RB','VBD'),('RBR','VBD'),('RBS','VBD'),('RB','VBN'),('RBR','VBN'),('RBS','VBN'),('RB','VBG'),('RBR','VBG'),('RBS','VBG')]
	wordTuples = list()
	# Extracting tuples in PosTag tuple list and put them into a list
	for w in range(1,(len(posList)-1)):
		[w1,t1] = posList[w]
		[w2,t2] = posList[w+1]
		tp = t1,t2
		bg = w1,w2
		if tp in tagTuples:
			if bg not in wordTuples:
				wordTuples.append(bg)
	return wordTuples

# Example:
# ts = TextSegmenter('www.bookdwarf.com/100t1.txt')
# print ts.process()
# Returns: [('recently', 'read'), ('new', 'collection'),...]