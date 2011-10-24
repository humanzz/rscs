import os
import sys
import re
from string import *
import nltk
import urllib
from os import listdir
import urlparse

workingDir = os.getcwd() + '/crawler_sources/'

# classes
class urlSite:
  def __init__(self,url,patterns):
    self.url=url
    self.patterns=patterns
    self.content=''
    self.textAdresses=[]
    self.hostname = urlparse.urlparse(url).hostname

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

def extractURLContents(url):
  f = urllib.urlopen(url.url)
  url.content = f.read()

def getTextAdress(url):
  for pat in url.patterns:
    url.textAdresses+=re.findall(pat,url.content, re.DOTALL)

def extractURLContentsFromAddress(url):
  f = urllib.urlopen(url)
  return f.read()

def downloadAddresses(url):
  print url.textAdresses
  for ad in url.textAdresses:
    
    f = urllib.urlopen(ad)
    
    html = f.read()
    # TODO create a file that says for each filename, what url it corresponds to
    urlDir = os.getcwd() + "/corpus/" + url.hostname + '/'
    if not os.path.exists(urlDir):
        os.makedirs(urlDir)
    i = 1
    fileName = lambda: urlDir + str(i) + ".html"
    while os.path.exists(fileName()):
      i = i+1
    text_file = open(fileName(), "w")
    text_file.write(html)
    text_file.close()

loadingURLDir(workingDir)
map(extractURLContents, urls)
map(getTextAdress, urls)
map(downloadAddresses, urls)