from __future__ import division 
import os
import re
import math
import time
from phrase_extractor import PhraseExtractor
from search import Search

class Scorer:
  phrasesRoot = os.getcwd() + "/phrases/"
  
  def score_phrases(input_file,output_file):
      # open files
      fi = open(Scorer.phrasesRoot+input_file, 'r')
      fo = open(Scorer.phrasesRoot+output_file, 'w')
      # get hits of "poor" and "excellent"
      hits_poor = Search.delayed_hits("poor",5)
      hits_exc = Search.delayed_hits("excellent",5)
      # iterate input file
      for phrase in fi:
          phrase = re.sub("\s+$","", phrase)
          # TODO: ADJUST THE TIMING DELAY
          hits_ph_poor = Search.delayed_hits("\""+phrase+"\" NEAR poor",5)
          hits_ph_exc = Search.delayed_hits("\""+phrase+"\" NEAR excellent",5)
          so = 0
          if(hits_ph_poor > 0 and hits_exc > 0 and hits_ph_exc > 0 and hits_poor > 0):
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
  Scorer.score_phrases("unscored.txt", "scored_10.txt")
  print ""

if __name__ == "__main__":
    main()

