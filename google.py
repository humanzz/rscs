# The Google AJAX API is deprecated
# They will limit how many searches we do
# Therefore we should build a table of all values we need to search for
# And store the results so that we don't need to repeat stuff

#import lxml.html as lh
import urllib
#import urllib2
#import mechanize
import simplejson

class Google:
  #def search(query):
  #  url = "http://www.google.com/search"
  #  params = urllib.urlencode({'hl': 'en', 'q': query, 'btnG': 'Google Search'})
  #  urlwp = url + '?' + params
  #  pagestr = Google.get_page(urlwp)
  #  print pagestr
  #  #doc = lh.fromstring(pagestr)
  #  #print doc.cssselect('#resultStats')
  #search = staticmethod(search)
  
  def jsearch(query):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + urllib.urlencode({'q': query})
    return simplejson.load(urllib.urlopen(url))
  jsearch = staticmethod(jsearch)
  
  #def get_page(url):
  #  req = mechanize.Request(url)
  #  req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.21 Safari/535.7')
  #  r = mechanize.urlopen(req)
  #  return r.read()
  #get_page = staticmethod(get_page)
    
res = Google.jsearch('ahmed AROUND(9) sobhi')
print res['responseData']['cursor']['estimatedResultCount']