#!/usr/bin/python
# -*- coding: utf-8 -*-

import jieba
import os
import sys
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer

reload(sys)
sys.setdefaultencoding('utf8')

wordslist = []
titlelist = []


def traversing_folder(dir):
    """遍历文件夹"""
    for file in os.listdir(dir):
        full_file_path = dir + "/" + file
        if os.path.isdir(full_file_path):
            traversing_folder(full_file_path)
        else:
            # windows下编码问题添加：.decode('gbk', 'ignore').encode('utf-8'))
            titlelist.append(file)
            with open(full_file_path, 'r') as f:
                content = f.read().strip().replace('\n', '').replace(
                    ' ', '').replace('\t', '').replace('\r', '')
            seg_list = jieba.cut(content, cut_all=True)
            result = ' '.join(seg_list)
            wordslist.append(result)


if __name__ == "__main__":
    yuliaoku_dir = os.path.join(os.getcwd(), 'yuliaoku')
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
            print(u'-{}: {} {}'.format(str(i + 1), words[loc[i]], w[loc[i]]))
        print('\n')
