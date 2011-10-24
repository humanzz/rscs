import os
import sys
import re
from string import *
import nltk
import urllib
from os import listdir
import urlparse

class urlSite:
  urlsRoot = os.getcwd() + '/crawler_sources/'
  corpusRoot = os.getcwd() + "/corpus/"
  
  def __init__(self,url,patterns):
    self.url=url
    self.patterns=patterns
    self.content=''
    self.textAdresses=[]
    self.hostname = urlparse.urlparse(url).hostname
  
  # Loads all url files from this directory
  # Returns an array of urlSite objects
  # if process is true, then for each urlSite, it will do all operations
  def fromDir(dir, process = False):
    urls = []
    for f in listdir(dir):
      if re.match('.+\.txt$',f):
        url = urlSite.fromFile(dir+f, process)
        if url:
          urls.append(url)
    return urls
  fromDir = staticmethod(fromDir)
  
  
  # Loads a url from the given object
  # Returns urlSite
  # If process is true, it downloads root content, extracts addresses and download pages
  def fromFile(fileName, process = False):
    url = None
    pats = []
    for line in map(lambda x:x.replace('\r','').replace('\n',''),open(fileName).readlines()):
      m = re.match('^root=(.+)$',line)
      if m:
        url=m.group(1)
        continue
      m = re.match('^1 pattern(.+)$',line)
      if m:
        pats.append(m.group(1))
        continue
    if url:
      us = urlSite(url,pats)
      if process:
        us.process()
      return us
  fromFile = staticmethod(fromFile)
  
  def downloadRootContent(self):
    self.content = urllib.urlopen(self.url).read()
  
  def extractAddressesFromRootContent(self):
    for pat in self.patterns:
      self.textAdresses += re.findall(pat,self.content, re.DOTALL)
    
  def downloadAddresses(self):
    urlDir = self.corpusRoot + self.hostname + '/'
    if not os.path.exists(urlDir):
        os.makedirs(urlDir)
    urlsFile = open(urlDir + 'all.urls', 'a')
    for ad in self.textAdresses:
      f = urllib.urlopen(ad)
      html = f.read()
      i = 1
      fileName = lambda: urlDir + str(i) + ".html"
      while os.path.exists(fileName()):
        i = i+1
      text_file = open(fileName(), "w")
      text_file.write(html)
      text_file.close()
      urlsFile.write('{0} {1}\n'.format(fileName(), ad))
    urlsFile.close()
    
  def process(self):
    self.downloadRootContent()
    self.extractAddressesFromRootContent()
    self.downloadAddresses()

#urls = urlSite.fromDir(urlSite.urlsRoot, False)
#urls[0].process()
urls = urlSite.fromDir(urlSite.urlsRoot, True)
