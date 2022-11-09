#Importing required module
import numpy as np
from nltk.tokenize import  word_tokenize
import nltk
nltk.download('punkt')
from creatdata import twowords
from creatdata import stopwords
import time
import json
from Suggest_news import news



start=time.time()


#print(len(twowords))

#------------------------------------some functions---------------------------------------------------------
def count_dict(sentences):
    word_count = {}
    for word in word_set:
        word_count[word] = 0
        for sent in sentences:
            if word in sent:
                word_count[word] += 1
    return word_count

#Term Frequency
def termfreq(document, word):
    N = len(document)
    occurance = len([token for token in document if token == word])
    return occurance/N

#Inverse Document Frequency
def inverse_doc_freq(word):
    try:
        word_occurance = word_count[word] + 1
    except:
        word_occurance = 1
    return np.log(total_documents/word_occurance)

#TF-IDF
def tf_idf(sentence):
    tf_idf_vec = np.zeros((len(word_set),))
    for word in sentence:
      if word in word_set:
        tf = termfreq(sentence,word)
        idf = inverse_doc_freq(word)
        value = tf*idf
        tf_idf_vec[index_dict[word]] = value
    return tf_idf_vec

#Cosine similarity
def cos_cal(vec_a,vec_b):
  cos_sim = np.inner(vec_a, vec_b)/(np.linalg.norm(vec_a)* np.linalg.norm(vec_b))
  return cos_sim

#jaccard similarity
def jaccard_similarity(A, B):

    tmp=0
    for i in range(len(A)):
        if A[i]==B[i]: tmp+=1

    return tmp/len(A)


#*********************************************************************************************

#Preprocessing the text data
sentences = []
word_set = []

with open("baothethao2.txt") as f:
  contents = f.readlines()

#print(contents)

for sent in contents:
    tmp=""
    check=False
    x = [i.lower() for  i in word_tokenize(sent) if i.isalpha()]
    sentences.append(x)
    check2=False
    for word in x:
        if check:
            check=False
            continue
        tmp2=tmp+word
        tmp = word + ' '
        if (tmp2 in twowords) and (tmp2 not in word_set):
            if check2: word_set.pop()
            word_set.append(tmp2)
            check = True
            check2=False
        elif (word in word_set) or (word in stopwords): continue
        else:
            word_set.append(word)
            check2=True
with open('result.txt', 'w', encoding='utf8') as json_file:
    json.dump(word_set, json_file, ensure_ascii=False)
json_file.close()
#print(len(word_set))

#Set of vocab
word_set = set(word_set)
#Total documents in our corpus
total_documents = len(sentences)

#Creating an index for each word in our vocab.
index_dict = {} #Dictionary to store index for each word
i = 0
for word in word_set:
    index_dict[word] = i
    i += 1
#Creating word_count
word_count = count_dict(sentences)
with open('count_dict.txt', 'w', encoding='utf8') as json_file:
    json.dump(word_count, json_file, ensure_ascii=False)
json_file.close()

#TF-IDF Encoded text corpus
vectors = []
for sent in sentences:
    vec = tf_idf(sent)
    vectors.append(vec)

#Creat user-vector
tf_words = {}
vec_user = []
total_words = 0
for sent in sentences:
    total_words += len(sent)

avg=0
jac_user_vec=[]

for word in word_set:
  tf_words[word] = 0
  for sent in sentences:
    if word in sent:
      for tmp_word in sent:
        if (word==tmp_word):
            tf_words[word] += 1/total_words

  avg+=tf_words[word]/len(word_set)

set(word_set)

with open('tf_word.txt', 'w', encoding='utf8') as json_file:
    json.dump(tf_words, json_file, ensure_ascii=False)
json_file.close()

for x,y in tf_words.items():
  if y>=avg: jac_user_vec.append(1)
  else: jac_user_vec.append(0)
  vec_user.append(y)

#print(vec_user)

#*********************************************************************************************
#Testing

'''with open("testingrss.txt") as fii:
  thethao = fii.readlines()'''

res_cos={}
link_title={}

for i in range(len(news)):
    sent=news[i]['content']
    x = [i.lower() for i in word_tokenize(sent) if i.isalpha()]
    sentences.append(x)

    t_vec=tf_idf(x)

    jac_t_vec=[]
    avg=0
    for value in t_vec:
        avg+=value/len(t_vec)
    for x in t_vec:
        if x>=avg: jac_t_vec.append(1)
        else: jac_t_vec.append(0)


    A = jac_user_vec
    B = jac_t_vec
    val=cos_cal(t_vec,vec_user)
    res_cos[news[i]['title']]=val
    link_title[news[i]['title']]=news[i]['link']
    sentences.pop()

res_cos={k: v for k, v in sorted(res_cos.items(), key=lambda item: item[1], reverse=True)}
#res_jac={k: v for k, v in sorted(res_jac.items(), key=lambda item: item[1], reverse=True)}
'''
for key in res_cos:
    print(key, ' : ', res_cos[key],'\n')

print('----------------------- \n')

"""
for key in res_jac:
    print(key, ' : ', res_jac[key],'\n')
"""

print("--- %s seconds ---" % (time.time() - start))
'''
print(link_title)