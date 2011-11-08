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

# ASK humanzz if you don't have that file
BING_APPID = open('bingappid','r').read()

class Search:
  def search(base, params):
    return simplejson.load(urllib.urlopen(base + urllib.urlencode(params)))
  search = staticmethod(search)
  
  def google(query):
    return Search.search('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&', {'q': query})
  google = staticmethod(google)
  
  def bing(query):
    return Search.search('http://api.bing.net/json.aspx?Version=2.2&Market=en-US&Web.Count=1&Sources=Web&JsonType=raw&', {'AppId': BING_APPID, 'Query': query})
  bing = staticmethod(bing)