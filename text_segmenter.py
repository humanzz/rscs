import os
import nltk
import string

class TextSegmenter:
  corpusRoot = os.getcwd() + "/corpus/"
  
  def __init__(self, filename):
    self.filename = filename # include directory path like "www.amazon.com/10t1.txt"
    self.filepath = self.corpusRoot + filename

  def isAdjAdv(self, x):
	tags = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']
	[word,posTag] = x
	return posTag in tags 
      
  def process(self):
	file = open(self.filepath,'r')
	text = file.read()
	# pos-tag the sentences
	words = nltk.word_tokenize(text)
	posList = nltk.pos_tag(words)
	#words_noP = [w for w in words if w not in string.punctuation]
	#tag1 = ['JJ', 'JJ', 'RB', 'RBR','RBS','JJ','NN','NNS','RB','RBR','RBS','RB','RBR','RBS','RB','RBR','RBS','RB','RBR','RBS']
	#tag2 = ['NN','NNS','JJ','JJ','JJ','JJ','JJ','JJ','VB','VB','VB','VBD','VBD','VBD','VBN','VBN','VBN','VBG','VBG','VBG']
	tagTuples = [('JJ','NN'),('JJ','NNS'),('RB','JJ'),('RBR','JJ'),('RBS','JJ'),('JJ','JJ'),('NN','JJ'),('NNS','JJ'),('RB','VB'),('RBR','VB'),('RBS','VB'),('RB','VBD'),('RBR','VBD'),('RBS','VBD'),('RB','VBN'),('RBR','VBN'),('RBS','VBN'),('RB','VBG'),('RBR','VBG'),('RBS','VBG')]
	wordTuples = list()
	for w in range(1,(len(posList)-1)):
		[w1,t1] = posList[w]
		[w2,t2] = posList[w+1]
		tp = t1,t2
		bg = w1,w2
		if tp in tagTuples:	
			wordTuples.append(bg)
	
	# filted to get only adjective and adverbs
	#filteredList = filter(self.isAdjAdv, posList)
	#return [x[0] for x in filteredList]
	return wordTuples
        
ts = TextSegmenter('www.bookdwarf.com/100t1.txt')
print ts.process()