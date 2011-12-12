import os, os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, ID

class Indexer:

    urlsRoot = os.getcwd() + '/crawler_sources/'
    corpusRoot = os.getcwd() + "/corpus/"
    indexdir = corpusRoot + "/index/"
    # TODO get proper corpus
    refCorpusRoot = os.getcwd()+'/corpus/test/'

    def add_documents(idx,rootdir):
        for root, subFolders, files in os.walk(rootdir):
            for file in files:
                filepath = os.path.join(root,file)
                f = open(filepath,"r")
                text_content = f.read()
                writer = idx.writer()
                writer.add_document(path=unicode(filepath), content=unicode(text_content))
                writer.commit()
                # print filepath
    add_documents = staticmethod(add_documents)

    def index(rootdir):
        # create schema
        schema = Schema(path=ID(stored=True),
                content=TEXT)
        # TODO we can stem the words in the index if we want to 
        # create index
        if not os.path.exists(Indexer.indexdir):
            os.mkdir(indexdir)
        idx = index.create_in(Indexer.indexdir, schema)
        # add documents to index
        Indexer.add_documents(idx,Indexer.refCorpusRoot)
    index = staticmethod(index)
    
    def get_index():
        if not os.path.exists(Indexer.indexdir):
            return indexer.index(Indexer.refCorpusRoot)
        else : 
            return index.open_dir(Indexer.indexdir)
    get_index = staticmethod(get_index)
    
# example usage 
Indexer.index(Indexer.refCorpusRoot)

