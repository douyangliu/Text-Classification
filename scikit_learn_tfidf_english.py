#!/usr/bin/python
# -*- coding: utf-8 -*-

# import jieba
import nltk
import os
import sys
import string
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from nltk.corpus import stopwords
from collections import Counter
from nltk.stem.porter import *


reload(sys)
sys.setdefaultencoding('utf8')

wordslist = []
titlelist = []


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def traversing_folder(dir):
    """遍历文件夹"""
    for file in os.listdir(dir):
        if '.' in file:
            continue
        full_file_path = dir + "/" + file
        if os.path.isdir(full_file_path):
            traversing_folder(full_file_path)
        else:
            # windows下编码问题添加：.decode('gbk', 'ignore').encode('utf-8'))
            titlelist.append(file)
            with open(full_file_path, 'r') as f:
                content = f.read().strip().replace('\n', '').replace('\t', '').replace('\r', '')
            lower = content.lower()
            no_punctuation = lower.translate(None, string.punctuation)
            tokens = nltk.word_tokenize(no_punctuation)
            filtered = [
                w for w in tokens if not w in stopwords.words('english')]
            # stemmer = PorterStemmer()
            # stemmed = stem_tokens(filtered, stemmer)
            result = ' '.join(filtered)
            wordslist.append(result)


if __name__ == "__main__":
    yuliaoku_dir = os.path.join(os.getcwd(), 'yuliaoku/english')
    traversing_folder(yuliaoku_dir)

    vectorizer = CountVectorizer()
    transformer = TfidfTransformer()
    tfidf = transformer.fit_transform(vectorizer.fit_transform(wordslist))

    words = vectorizer.get_feature_names()  # 所有文本的关键字
    weight = tfidf.toarray()

    n = 3  # 前五位
    for (title, w) in zip(titlelist, weight):
        print(u'{}:'.format(title))
        # 排序
        loc = np.argsort(-w)
        for i in range(n):
            print(u'-{}: {} {}'.format(str(i + 1),
                                       words[loc[i]], round(w[loc[i]], 5)))
        print('\n')
