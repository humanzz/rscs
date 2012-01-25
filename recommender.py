import os
import re
import random
import operator
from scorer import Scorer

class Recommender:
  phrasesRoot = os.getcwd() + "/phrases/"
  corpusRoot = os.path.join(os.getcwd(), "corpus")
  
  def __init__(self, filename="scored.txt"):
    self.scorer = Scorer()
  
  # Calculates the semantic orientation of all products
  # based on their reviews and outputs a list of them
  # ordered descendingly
  def recommend(self, filename="recommendations.txt"):
    scores = {}
    nscores = {} # how many reviews for that product
    for d in os.listdir(Recommender.corpusRoot):
      if os.path.isdir(os.path.join(Recommender.corpusRoot, d)):
        for f in os.listdir(os.path.join(Recommender.corpusRoot, d)):
          m = re.search("(\d+)t(\d+).txt",f)
          if m:
            key = "{0}-{1}".format(d,m.groups()[0])
            so = self.scorer.file_semantic_orientation(os.path.join(Recommender.corpusRoot, d, f))
            if key in scores:
              scores[key] = scores[key] + so
              nscores[key] = nscores[key] + 1
            else:
              scores[key] = so
              nscores[key] = 1
    for key in scores:
      scores[key] = scores[key]/nscores[key] #averaging multiple reviews for the same product
    
    scores = sorted(scores.iteritems(), key=operator.itemgetter(1), reverse = True)
    if filename:
      f = open(filename,"w")
      for score in scores:
        f.write('{0} {1}\n'.format(score[0],score[1]))
      f.close()
    return scores
              
def main():
  r = Recommender("scorede.txt")
  r.recommend("recommendationse.txt")

if __name__ == "__main__":
    main()

