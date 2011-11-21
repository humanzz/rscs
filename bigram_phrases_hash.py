import os
import nltk
import string

class PhraseScorer:
  corpusRoot = os.getcwd() + "/corpus2/"
  
  def all_corpus_phrases():
	bigrams = {}
	
	dirList = os.listdir("./")
	for d in dirList:
		listing = os.listdir(corpusRoot)
		for infile in listing:
			if re.match('.+\.txt$',infile):
				fillHash(bigrams,infile)

	return bigrams

	#all_corpus_phrases = staticmethod(all_corpus_phrases)
  
  # def write_all_corpus_phrases():
	#iterate over hash and write it to text file
	# write_all_corpus_phrases = staticmethod(write_all_corpus_phrases)
  
  def __init__(self, score_file):
    self.filename = score_file # include directory path like "www.amazon.com/10t1.txt"
    self.filepath = self.corpusRoot + score_file
      
  def fillHash(self,hashPhrases,fileName):
	file = open(fileName,'r')
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
			if tp not in hashPhrases:
				hashPhrases['{0} {1}'.format(w1, w2)] = True

				
				
PhraseScorer('ruby.txt').all_corpus_phrases()
# Example:
# ts = TextSegmenter('www.bookdwarf.com/100t1.txt')
# print ts.process()
# Returns: [('recently', 'read'), ('new', 'collection'),...]