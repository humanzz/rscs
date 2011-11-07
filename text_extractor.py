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
    elif self.hostname.find('blogspot') > -1:
        text = ''
        # get title
        for divTitle in doc.cssselect('h3.post-title.entry-title a'):
            text += divTitle.text_content()
        # get content
        for divContent in doc.cssselect('.post-body entry-content'):
             text += divContent.text_content()
        result[1] = text
    elif self.hostname.find('wordpress') > -1:
        text = ''
        # get title
        for divTitle in doc.cssselect('.posttitle h2'):
            text += divTitle.text_content()
        # get content
        for divContent in doc.cssselect('.entry'):
             text += divContent.text_content()
        result[1] = text
    elif self.hostname == 'www.shvoong.com':
        text = ''
        # get content
        for divContent in doc.cssselect('.shvoongsummarizer'):
             text += divContent.text_content()
        result[1] = text
    elif self.hostname == 'www.bookdwarf.com':
        text = ''
        # get content
        for divContent in doc.cssselect('.post-bodycopy.clearfix'):
             text += divContent.text_content()
        result[1] = text
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
        
te = TextExtractor('www.bookdwarf.com')
te.process()