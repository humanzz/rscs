import os
import sys
import re
from string import *
import nltk
import urllib
from os import listdir

workingDir = os.getcwd() + '/crawler_sources/'

# classes
class urlSite:
  def __init__(self,url,patterns):
    self.url=url
    self.patterns=patterns
    self.content=''
    self.textAdresses=[]

# auxiliar
def _encode(data):
  return data.encode('utf8')

def _decode(data):
  return data.decode('utf8')

def loadingURLDir(d):
  global urls
  urls=[]
  for f in listdir(d):
    if re.match('.+\.txt$',f):
      url = loadingURLFile(d+f)
      if url:
        urls.append(url)

def loadingURLFile(f):
  url = None
  pats=[]
  for line in map(lambda x:x.replace('\r','').replace('\n',''),open(f).readlines()):
    m = re.match('^root=(.+)$',line)
    if m:
      url=m.group(1)
      continue
    m = re.match('^1 pattern(.+)$',line)
    if m:
      pats.append(m.group(1))
      continue
  if url:
    return urlSite(url,pats)
        
def extractURLContents():
  global urls
  for i in urls:
    print 'opening ' + i.url
    f = urllib.urlopen(i.url)
    i.content=f.read()
    
def getTextAdresses():
  global urls
  for i in urls:
    for j in i.patterns:
      i.textAdresses+=re.findall(j,i.content, re.DOTALL)

def extractURLContentsFromAddress(url):
  f = urllib.urlopen(url)
  return f.read()

def downloadAddresses(url):
  for ad in url.textAdresses:
    f = urllib.urlopen(ad)
    html = f.read()
    #text = nltk.clean_html(html)
    i = 1
    # TODO should change this lambda to use the domain name
    fileName = lambda: os.getcwd() + "/corpus/text" + str(i) + ".html"
  
    while os.path.exists(fileName()):
          i = i+1
    text_file = open(fileName(), "w")
    text_file.write(html)
    text_file.close()


loadingURLDir(workingDir)
extractURLContents()
getTextAdresses()
map(downloadAddresses,urls)
#for url in urls:
#  print len(url.content)
#  print url.patterns
#  for address in url.textAdresses:
#    print address