# COUNT DOCUMENT
import glob
import os

file_list = glob.glob(os.path.join(os.getcwd(), "/home/danu/Downloads", "*.txt"))

raw_documents = []

for file_path in file_list:
    with open(file_path, encoding="latin1") as f_input:
        raw_documents.append(f_input.read())

print("Number of documents:",len(raw_documents))

#  COUNT Word
import gensim
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
gen_docs = [[w.lower() for w in word_tokenize(text)] 
            for text in raw_documents]
print(gen_docs)

dictionary = gensim.corpora.Dictionary(gen_docs)
print(dictionary[3])
print(dictionary.token2id['today'])
print("Number of words in dictionary:",len(dictionary))
for i in range(len(dictionary)):
    print(i, dictionary[i])

corpus = [dictionary.doc2bow(gen_doc) for gen_doc in gen_docs]
print(corpus)

print ("")
print ("NEW SEGMENT : ")

tf_idf = gensim.models.TfidfModel(corpus)
print(tf_idf)

print ("")
print ("FILTER % : ")
query_doc = [w.lower() for w in word_tokenize("databases")]
print(query_doc)
query_doc_bow = dictionary.doc2bow(query_doc)
print(query_doc_bow)
# query_doc_tf_idf = tf_idf[query_doc_bow]
# print(query_doc_tf_idf)

print ("")
# print ("RESULT : ")
# from gensim.matutils import softcossim
# import gensim.downloader as api
# fasttext_model300 = api.load('fasttext-wiki-news-subwords-300')
# similarity_matrix = fasttext_model300.similarity_matrix(dictionary, tfidf=None, threshold=0.0, exponent=2.0, nonzero_limit=100)
# softcossim(corpus[0], corpus[5],similarity_matrix)
# similar_docs = gensim.similarities.Similarity('zone/text_mining/document_similarity',tf_idf[corpus],
#                                       num_features=len(dictionary))
# similar_docs
# similar_docs[query_doc_tf_idf]

