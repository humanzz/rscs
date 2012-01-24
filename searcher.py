from whoosh import index
from whoosh import query, spans
from whoosh.qparser import QueryParser
from indexer import Indexer

class Searcher:

    def search_near(idx,word1,word2,distance):
        with idx.searcher() as s:
            qp = QueryParser("content", schema=idx.schema)
            # TODO stem word1 word2 if we stem the index
            t1 = query.Term("content", word1)
            t2 = query.Term("content", word2)
            q = spans.SpanNear(t1, t2, slop=distance)
            res = s.search(q)
            # TODO we can return only len(res).
            # The problem of returning the res object is that somehow
            # we won't be able to call len(res) outside of this function 
            # i dunno whyyyy :s
            return len(res) 
    search_near = staticmethod(search_near)
    
    def search(idx,word):
        with idx.searcher() as s:
            qp = QueryParser("content", schema=idx.schema)
            q = qp.parse(unicode(word))
            res = s.search(q)
            return len(res)
    search = staticmethod(search)
    
# example usage
idx = Indexer.get_index()
# res = Searcher.search_near(idx, "was", "she", 5)
# print res
res = Searcher.search(idx,"billion")
print res

# to investigate words in the corpus
#try:
#    idx = Indexer.get_index()
#    searcher = idx.searcher()
#    contents = list(searcher.lexicon("content"))
#    print contents
#finally:
#    searcher.close()
