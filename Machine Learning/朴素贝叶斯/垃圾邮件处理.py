import numpy as np
import beyes
import re
from sklearn.model_selection import train_test_split
def textParse(bigstring):
    listOfTokens = re.split(r'\W+',bigstring)
    return [tok.lower() for tok in listOfTokens if len(tok) >0]
def spamTest():
    doclist = []
    classlist = []
    fullTest = []
    pre = []
    error = 0
    accuracy = 0
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
    X_trian,X_test,y_train,y_test = train_test_split(veclist,classlist,test_size = 0.2,random_state = 17)
    p1vect,p0vect,pAbusive = beyes.train_model(X_trian,y_train)
    for i in range(X_test.shape[0]):
        pre.append(beyes.pre_classify(X_test[i],p1vect,p0vect,pAbusive))
        if pre[i] != y_test[i]:
            error += 1
        print(f"{i} the predict is {pre[i]}, the real result is {y_test[i]}")
    accuracy = (X_test.shape[0] - error) / X_test.shape[0]
    print(f'the total error is {error}')
    print(f'the accuracy is {accuracy}')
spamTest()

