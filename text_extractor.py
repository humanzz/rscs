import lxml.html as lh
import os
from os import listdir
import re

class TextExtractor:
  corpusRoot = os.getcwd() + "/corpus/"
  
  def __init__(self, hostname):
    self.hostname = hostname
    self.directory = self.corpusRoot + hostname + '/'
  
  def extractTexts(self, file):
    result = {}
    doc = lh.fromstring(open(file).read())
    # TODO if else if here for the different cases we can handle
    if self.hostname == 'www.amazon.com':
      i = 1
      # select the div that contains the review text. Unfortunately,
      # text is not contained in a clear container
      for div in doc.cssselect('#productReviews td div[style^="margin-left:0.5em"]'):
        text = ''
        # take long enough texts under that div hoping it will be part of the review
        for txt in div.itertext():
          # number chosen arbitrarily
          if len(txt) > 125:
            text += txt
        result[i] = text
        i+=1
    return result
  
  def processFile(self, f):
    texts = self.extractTexts(f)
    prefix = re.match('^(.+)\.html', f).group(1)
    for key in texts:
      f = open(prefix + 't' + str(key) + '.txt', 'w')
      f.write(texts[key].encode('utf8'))
      f.close()
    
  def process(self):
    for f in listdir(self.directory):
      if re.match('.+\.html$',f):
        self.processFile(self.directory + f)
        
#te = TextExtractor('www.amazon.com')
#te.process()