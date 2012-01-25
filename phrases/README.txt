This document provides a description of the different components used in this recommendation system

urlSite
	This is the class responsible to crawl the websites listed in crawler_cources directory. It downloads the html files representing those pages to build the corpus
	
TextExtractor
	This is responsible for extracting the textual content of the html files and storing them in separate text files
	
PhraseExtractor
	This is responsible for processing all the text files in the corpus and extract all phrases (bigrams) according to some selection criteria to store them in a file listing all possible phrases
	
Scorer
	It has 2 main responsibilities:
	1. Calculate the Semantic Orientation scores for all the phrases in the file produced by the PhraseExtractor
	2. Calculate the SO score for different texts
	
Search
	Used by Scorer to connect to search engines to get the number of hits and calculate SO scores
	
Recommender
	It uses the scorer to calculate the SO of all products and sort them based on their SO scores
	
Statistics
	To calculate some statistics about the corpus
	

