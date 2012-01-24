import os, os.path
from whoosh import index
from whoosh.fields import Schema, TEXT, ID
from nltk.corpus import reuters

class Indexer:

    urlsRoot = os.getcwd() + '/crawler_sources/'
    indexdir = os.getcwd() + "/index/"
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
            os.mkdir(Indexer.indexdir)
        idx = index.create_in(Indexer.indexdir, schema)
        # add documents to index
        Indexer.add_documents(idx,Indexer.refCorpusRoot)
    index = staticmethod(index)
    
    def index_reuters():
        # create schema
        schema = Schema(path=ID(stored=True),
                content=TEXT)
        # TODO we can stem the words in the index if we want to 
        # create index
        if not os.path.exists(Indexer.indexdir):
            os.mkdir(Indexer.indexdir)
        idx = index.create_in(Indexer.indexdir, schema)
        # add reuters files
        fileIds = reuters.fileids()
        for i in fileIds:
            print i
            text_content = reuters.raw(i)
            print text_content
            writer = idx.writer()
            writer.add_document(path=unicode(i), content=unicode(text_content))
            writer.commit()
            # TO BE DELETED!!
            if (i=="test/14903"):
                break
        return idx
    index_reuters = staticmethod(index_reuters)
    
    def get_index():
        if not os.path.exists(Indexer.indexdir):
            # return indexer.index(Indexer.refCorpusRoot)
            return Indexer.index_reuters()
        else : 
            return index.open_dir(Indexer.indexdir)
    get_index = staticmethod(get_index)
    
# example usage 
# Indexer.index(Indexer.refCorpusRoot)
# Indexer.index_reuters()
Indexer.get_index()
