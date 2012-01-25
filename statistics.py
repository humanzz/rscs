import os
import nltk
import string
import re
from phrase_extractor import PhraseExtractor


# This module's purpose is to get statistics from the reviews:
# - phrases per review: mean max average
# - bigram of the review: mean max average
class Statistics:
  corpusRoot = os.path.join(os.getcwd(), "corpus")
  
  tagTuples = [('JJ','NN'),('JJ','NNS'),('RB','JJ'),('RBR','JJ'),('RBS','JJ'),
               ('JJ','JJ'),('NN','JJ'),('NNS','JJ'),('RB','VB'),('RBR','VB'),
               ('RBS','VB'),('RB','VBD'),('RBR','VBD'),('RBS','VBD'),('RB','VBN'),
               ('RBR','VBN'),('RBS','VBN'),('RB','VBG'),('RBR','VBG'),('RBS','VBG')]
  
  # Get statistics from the whole corpus
  def get_corpus_stat():
    bigrams = {}
    maxBigram = 0
    minBigram = 999999
    totalBigram = 0
    n = 0
    minPhrase = 999999
    maxPhrase = 0
    totalPhrase = 0
    for d in os.listdir(Statistics.corpusRoot):
      if os.path.isdir(os.path.join(Statistics.corpusRoot, d)):
        for f in os.listdir(os.path.join(Statistics.corpusRoot, d)):
          if re.match('.+\.txt$',f):
            nbBigram, nbPhrase = Statistics.get_file_stat(os.path.join(Statistics.corpusRoot, d, f))
            totalBigram = totalBigram + nbBigram
            totalPhrase = totalPhrase + nbPhrase
            if nbBigram > maxBigram:
                maxBigram = nbBigram
            if nbBigram < minBigram:
                minBigram = nbBigram
            if nbPhrase > maxPhrase:
                maxPhrase = nbPhrase
            if nbPhrase < minPhrase:
                minPhrase = nbPhrase
            n = n+1
    avgBigram = 0
    avgPhrase = 0
    if n>0:
        avgBigram = totalBigram/n
        avgPhrase = totalPhrase/n
    return maxBigram, minBigram, avgBigram, minPhrase, maxPhrase, avgPhrase
  get_corpus_stat = staticmethod(get_corpus_stat)
      
  # Get number of bigram and number of phrases in a file
  def get_file_stat(fileName):
    hashPhrases = {}
    file = open(fileName,'r')
    text = file.read()
    file.close()
    # pos-tag the sentences
    words = nltk.word_tokenize(text)
    posList = nltk.pos_tag(words)
    # list of all PosTag Tuples that we want to extract
    wordTuples = list()
    # Extracting tuples in PosTag tuple list and put them into a list
    nbBigram = 0
    nbPhrases = 0
    for w in range(1,(len(posList)-1)):
      [w1,t1] = posList[w]
      [w2,t2] = posList[w+1]
      tp = t1,t2
      bg = w1,w2
      nbBigram = nbBigram + 1
      if tp in PhraseExtractor.tagTuples:
        if tp not in hashPhrases:
            hashPhrases['{0} {1}'.format(w1, w2)] = True
            nbPhrases = nbPhrases + 1
    if nbBigram == 0:
      print "0 bigrams found in: {0}".format(fileName)
    return nbBigram, nbPhrases
  get_file_stat = staticmethod(get_file_stat)

maxBigram, minBigram, avgBigram, minPhrase, maxPhrase, avgPhrase = Statistics.get_corpus_stat()
print "max bigram: " + str(maxBigram)
print "min bigram: " + str(minBigram)
print "avg bigram: " + str(avgBigram)
print "min phrase: " + str(minPhrase)
print "max phrase: " + str(maxPhrase)
print "avg phrase: " + str(avgPhrase)