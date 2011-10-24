import lxml.html as lh
import nltk
import os

file = os.getcwd() + '/1.html'
doc = lh.fromstring(open(file).read())

for div in doc.cssselect('.post-bodycopy.clearfix'):
  #print(div.text_content())
