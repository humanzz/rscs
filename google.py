# The Google AJAX API is deprecated
# They will limit how many searches we do
# Therefore we should build a table of all values we need to search for
# And store the results so that we don't need to repeat stuff
# Example usage for us
# res = Google.jsearch('ahmed AROUND(9) sobhi')
# print res['responseData']['cursor']['estimatedResultCount']

import urllib
import simplejson

class Google:  
  def jsearch(query):
    url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + urllib.urlencode({'q': query})
    return simplejson.load(urllib.urlopen(url))
  jsearch = staticmethod(jsearch)