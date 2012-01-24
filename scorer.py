import os
import re
import math
from searcher import Searcher
from indexer import Indexer

class Scorer:
  phrasesRoot = os.getcwd() + "/phrases/"
  
  def score_phrases(input_file,output_file,distance):
      # open files
      fi = open(Scorer.phrasesRoot+input_file, 'r')
      fo = open(Scorer.phrasesRoot+output_file, 'w')
      # get hits of "poor" and "excellent"
      idx = Indexer.get_index()
      hits_poor = Searcher.search(idx,"poor")
      hits_exc = Searcher.search(idx,"excellent")
      # iterate input file
      # TO BE DELETED!!
      i = 1
      for phrase in fi:
          i = i+1
          phrase = re.sub("\s+$","", phrase)
          hits_ph_poor = Searcher.search_near(idx,phrase,"poor",distance)
          hits_ph_exc = Searcher.search_near(idx,phrase,"exc",distance)
          so = 0
          if(hits_ph_poor > 0 and hits_exc > 0):
              so = math.log((hits_ph_exc * hits_poor)/(hits_ph_poor * hits_exc),2)
          print so
          fo.write(phrase+" "+str(so)+"\n")
          if(i>10):
              break
      fi.close()
      fo.close()
  score_phrases = staticmethod(score_phrases)
  
Scorer.score_phrases("unscored.txt", "scored_10.txt", 10)