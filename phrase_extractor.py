import os
import nltk
import string
import re


# This module's purpose is to extract all possible tuples from the corpus
# Example usages are as follows:
#   bigrams = PhraseExtractor.all_corpus_phrases()
#   bigrams = PhraseExtractor.file_phrases(os.path.join(PhraseExtractor.corpusRoot, "www.amazon.com", "1t1.txt"),{})
#   PhraseExtractor.write_all_corpus_phrases(PhraseExtractor.all_corpus_phrases())
class PhraseExtractor:
  #corpusRoot = os.path.join(os.getcwd(), "corpus")
  #phrasesRoot = os.path.join(os.getcwd(), "phrases")
  corpusRoot = os.path.join(os.getcwd(), "corpus_big")
  phrasesRoot = os.path.join(os.getcwd(), "phrases_big")
  
  tagTuples = [('JJ','NN'),('JJ','NNS'),('RB','JJ'),('RBR','JJ'),('RBS','JJ'),
               ('JJ','JJ'),('NN','JJ'),('NNS','JJ'),('RB','VB'),('RBR','VB'),
               ('RBS','VB'),('RB','VBD'),('RBR','VBD'),('RBS','VBD'),('RB','VBN'),
               ('RBR','VBN'),('RBS','VBN'),('RB','VBG'),('RBR','VBG'),('RBS','VBG')]
  
  def all_corpus_phrases():
    bigrams = {}
    
    for d in os.listdir(PhraseExtractor.corpusRoot):
      if os.path.isdir(os.path.join(PhraseExtractor.corpusRoot, d)):
        for f in os.listdir(os.path.join(PhraseExtractor.corpusRoot, d)):
          if re.match('.+\.txt$',f):
            PhraseExtractor.fillHash(bigrams,os.path.join(PhraseExtractor.corpusRoot, d, f))

    return bigrams
  all_corpus_phrases = staticmethod(all_corpus_phrases)
  
  def file_phrases(infile, bigrams = {}):
    return PhraseExtractor.fillHash(bigrams, infile)
  file_phrases = staticmethod(file_phrases)

  
  def write_all_corpus_phrases(bigrams,outfilename="unscored.txt"):
    f = open(os.path.join(PhraseExtractor.phrasesRoot,outfilename), "w")
    erroneus_count = 0
    for phrase in bigrams:
      try:
        f.write((phrase+"\n").encode('utf8'))
      except:
        erroneus_count = erroneus_count + 1
    f.close()
    print "{0} erroneous bigrams".format(erroneus_count)
  write_all_corpus_phrases = staticmethod(write_all_corpus_phrases)
      
  def fillHash(hashPhrases,fileName):
    file = open(fileName,'r')
    text = file.read()
    file.close()
    # pos-tag the sentences
    words = nltk.word_tokenize(text)
    posList = nltk.pos_tag(words)
    # list of all PosTag Tuples that we want to extract
    
    wordTuples = list()
    # Extracting tuples in PosTag tuple list and put them into a list
    for w in range(1,(len(posList)-1)):
      [w1,t1] = posList[w]
      [w2,t2] = posList[w+1]
      tp = t1,t2
      bg = w1,w2
      if tp in PhraseExtractor.tagTuples:
        if tp not in hashPhrases:
          hashPhrases['{0} {1}'.format(w1, w2)] = True
    return hashPhrases
  fillHash = staticmethod(fillHash)

#PhraseExtractor.write_all_corpus_phrases(PhraseExtractor.file_phrases(os.path.join(PhraseExtractor.corpusRoot, "www.amazon.com", "1t1.txt")))
#PhraseExtractor.write_all_corpus_phrases(PhraseExtractor.all_corpus_phrases())