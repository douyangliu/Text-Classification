import jieba
from collections import Counter
import math
from collections import defaultdict

copus=['我正在学习计算机','它正在吃饭','我的书还在你那儿','今天不上班']
copus= [[word for word in jieba.cut(doc)] for doc in copus]
print(copus)
tf = []
for doc in copus:
    tf.append(Counter(doc))
print(tf)


idf = defaultdict(int)
for doc in tf:
    for word in doc:
        idf[word] += 1
for word in idf:
    idf[word] = math.log(len(idf)/(idf[word]+1))
print(idf)
