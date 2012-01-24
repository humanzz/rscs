import os
import re
from phrase_extractor import PhraseExtractor

class Scorer:
  phrasesRoot = os.getcwd() + "/phrases/"
  
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
  scorer = Scorer()
  print scorer.scores
  print scorer.semantic_orientation({"weird cover":3,"popular radio":2, "new trend":1})

if __name__ == "__main__":
    main()
  