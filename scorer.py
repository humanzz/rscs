import os
import re
import math
import time
from searcher import Searcher
from indexer import Indexer
from phrase_extractor import PhraseExtractor
from search import Search

class Scorer:
  phrasesRoot = os.getcwd() + "/phrases/"
  
  def score_phrases(input_file,output_file,distance):
      # open files
      fi = open(Scorer.phrasesRoot+input_file, 'r')
      fo = open(Scorer.phrasesRoot+output_file, 'w')
      # get hits of "poor" and "excellent"
      idx = Indexer.get_index()
#      hits_poor = Searcher.search(idx,"poor")
      hits_poor = Search.delayed_hits("poor")
#      hits_exc = Searcher.search(idx,"excellent")
      hits_exc = Search.delayed_hits("excellent")
      # iterate input file
      for phrase in fi:
          print phrase
          phrase = re.sub("\s+$","", phrase)
          print Searcher.search(idx,phrase)
#          hits_ph_poor = Searcher.search_near(idx,phrase,"poor",distance)
          hits_ph_poor = Search.delayed_hits("\""+phrase+"\" NEAR poor")
          print hits_ph_poor
#          hits_ph_exc = Searcher.search_near(idx,phrase,"exc",distance)
          hits_ph_exc = Search.delayed_hits("\""+phrase+"\" NEAR excellent")
          print hits_ph_exc
          so = 0
          if(hits_ph_poor > 0 and hits_exc > 0):
              so = math.log((hits_ph_exc * hits_poor)/(hits_ph_poor * hits_exc),2)
          fo.write(phrase+" "+str(so)+"\n")
          fo.flush()
      fi.close()
      fo.close()
  score_phrases = staticmethod(score_phrases)
  

  def __init__(self, filename="scored.txt"):
    self.filename = os.path.join(Scorer.phrasesRoot, filename)
    self.scores = {}
    f = open(self.filename, "r")
    for line in f:
      m = re.search("(.+\s.+)\s(.+)", line)
      self.scores[m.groups()[0]] = float(m.groups()[1])
    f.close()

  # Takes an array or hash of phrases
  # and calculates their average semantic orientation
  def semantic_orientation(self, phrases):
    so = 0
    length = 0
    for phrase in phrases:
      if phrase in self.scores:
        so = so + self.scores[phrase]
        length = length + 1
    so = so / length
    return so

  # Reads a file, extracts relevant phrases and
  # returns their average semantic orientation
  def file_semantic_orientation(self,filename):
    file_phrases = {}
    PhraseExtractor.fillHash(file_phrases, filename)
    return self.semantic_orientation(file_phrases)



    
def main():
  #scorer = Scorer()
  #print scorer.scores
  #print scorer.semantic_orientation({"weird cover":3,"popular radio":2, "new trend":1})
  Scorer.score_phrases("unscored.txt", "scored_10.txt", 10)
  print ""

if __name__ == "__main__":
    main()

