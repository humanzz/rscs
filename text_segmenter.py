import os
import nltk

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
    # filter to get only adjective and adverbs
    filteredList = filter(self.isAdjAdv, posList)
    return [x[0] for x in filteredList]
        
#ts = TextSegmenter('www.bookdwarf.com/100t1.txt')
#print ts.process()