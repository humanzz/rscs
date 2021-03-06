# A simple Search JSON API
#   Googe AJAX API which is now deprecated. It works but they limit its usage
#   Bing is supposedly unlimited in usage
#
# For Proximity Search
#   Google
#   res = Google.jsearch('ahmed AROUND(9) sobhi')
#   print res['responseData']['cursor']['estimatedResultCount']
#
#   Bing
#   res = Search.bing("ahmed near:9 sobhi")
#   print res['SearchResponse']['Web']['Total']

import urllib
import simplejson
import pprint
import time

# ASK humanzz if you don't have that file
BING_APPID = open('bingappid','r').read()

class Search:
  def search(base, params):
    #print base + urllib.urlencode(params)
    return simplejson.load(urllib.urlopen(base + urllib.urlencode(params)))
  search = staticmethod(search)
  
  def google(query):
    return Search.search('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&', {'q': query})
  google = staticmethod(google)
  
  def bing(query):
    return Search.search('http://api.bing.net/json.aspx?Version=2.2&Market=en-US&Web.Count=1&Sources=Web+News+RelatedSearch&JsonType=raw&', {'AppId': BING_APPID, 'Query': query})
  bing = staticmethod(bing)
  
  def hits(query, search_engine = "bing"):
    res = getattr(Search, search_engine)(query)
    #print res['SearchResponse'].keys()
    #print res['SearchResponse']['News'].keys(), res['SearchResponse']['News']['Total'], res['SearchResponse']['News']['Results']
    if search_engine == "bing":
      if 'SearchResponse' in res and 'Web' in res['SearchResponse']:
        res = res['SearchResponse']['Web']['Total']
      else:
        res = 0
    elif search_engine == "google":
      res = res['responseData']['cursor']['estimatedResultCount']
      
    print '{0}: {1}'.format(query, res)
    return res
  hits = staticmethod(hits)
  
  def delayed_hits(query, delay=1, search_engine = "bing"):
    time.sleep(delay)
    return Search.hits(query, search_engine)
  delayed_hits = staticmethod(delayed_hits)
  
  def hits_near(phrase, near_to, search_engine = "bing"):
    return Search.hits('"{0}" near:9 {1}'.format(phrase, near_to), search_engine)
  hits_near = staticmethod(hits_near)
  
#print Search.hits("ahmed near:9 sobhi")
#print Search.hits_near("audi r8", "excellent")
#pprint.pprint(Search.bing("\"negative parts\" NEAR poor"))