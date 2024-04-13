import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import tree
import re
import beyes
def textParse(bigstring):
    listOfTokens = re.split(r'\W+',bigstring)   # 注意w大小写
    return [tok.lower() for tok in listOfTokens if len(tok) >0]
def dataset():
    doclist = []
    classlist = []
    fullTest = []
    for i in range(1,26):
        wordlist = textParse(open('email/spam/%d.txt'%i).read())
        # 打开文件的方法
        doclist.append(wordlist)
        fullTest.append(wordlist)
        classlist.append(1)
        wordlist = textParse(open('email/ham/%d.txt'%i).read())
        doclist.append(wordlist)
        fullTest.append(wordlist)
        classlist.append(0)
    vocablist = beyes.createVocabList(doclist)
    print(vocablist)
    lenof = len(fullTest)
    veclist = []
    for i in range(lenof):
        veclist.append(beyes.setofWordsVec(vocablist, fullTest[i]))
    veclist = np.array(veclist)
    return veclist,classlist
data,target = dataset()
X_trian, X_test, y_train, y_test = train_test_split(data, target, test_size=0.2, random_state=17)
clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(X_trian,y_train)
score = clf.score(X_test,y_test)
print(score)
pre = clf.predict(X_test)
error = 0
for i in range(len(pre)):
    print(f'the predict is {pre[i]}, the real result is {y_test[i]}')
    if pre[i] != y_test[i]:
        error += 1
print(f'the total error is {error}')