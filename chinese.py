from collections import Counter,defaultdict
import jieba
import math
 
def file2list(file):
    '''
    把文件转换成列表，并对数据进行简单的预处理
    '''
    with open(file) as f:
        corpus = f.readlines()
        corpus = [[word.replace('\n','') for word in jieba.cut(line)] for line in corpus if line.strip()]
    return corpus
#c = file2list('E:\hei.txt')
def get_tf(corpus):
    return [Counter(doc) for doc in corpus]#用Counter函数把每篇文档转换成词和词频的字典
def get_idf(tf_dict):
    idf = defaultdict(int)
    for doc in tf_dict:
        for word in doc:
            idf[word] += 1
    for word in idf:
        idf[word] = math.log(len(idf)/(idf[word]+1))#idf的公式
    return idf
 
def get_tfidf(doc_id,file):
    '''doc_id是语料库中文档的id，file是txt的路径'''
    corpus = file2list(file)
    tf = get_tf(corpus)
    idf = get_idf(tf)
    if doc_id > len(tf):
        print("doc_id should smaller than %i"%len(tf))
    else:
        id_tf= tf[doc_id-1]
        for word in id_tf:
            id_tf[word] = id_tf[word]*idf[word]#计算tfidf值
        print(id_tf)


 for word in id_tf:
            id_tf[word] = id_tf[word]*idf[word]#计算tfidf值
        print(id_tf)