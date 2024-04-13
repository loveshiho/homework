import numpy as np
def loadDataSet():
    postingList = [ ['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                    ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                    ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                    ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                    ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                    ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec
def createVocabList(dataset):
    vocabSet = set([])
    for document in dataset:
        vocabSet = vocabSet | set(document)
    return list(vocabSet)
def setofWordsVec(vocablist,onedataset):
    Vec = [0]*len(vocablist)
    for word in onedataset:
        if word in vocablist:
            Vec[vocablist.index(word)] = 1
    return Vec
def train_model(Veclist,target):
    numTrain = len(Veclist)
    numWords = len(Veclist[0])
    pAbusive = sum(target) / float(numTrain)
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)  # 防止概率为0，初始化为1.
    p0Denom = 2.
    p1Denom = 2.
    for i in range(numTrain):
        if target[i] == 1:
            p1Num += Veclist[i]
            p1Denom += sum(Veclist[i])
        else:
            p0Num += Veclist[i]
            p0Denom += sum(Veclist[i])
    p1Vect = np.log(p1Num / p1Denom)
    p0Vect = np.log(p0Num / p0Denom)
    pAbusive = np.log(pAbusive)
    # 防止概率过小，四舍五入，最终概率得0。
    return p0Vect,p1Vect,pAbusive
def pre_classify(input_vec,p0vect,p1vect,pAbusive):
    p1 = sum(input_vec * p1vect) + pAbusive
    p0 = sum(input_vec * p0vect) + 1 - pAbusive
    if p1 > p0:
        return 1
    else:
        return 0
def test_model():
    data,target = loadDataSet()
    vocablist = createVocabList(data)
    print(vocablist)
    Veclist = []
    for i in range(len(data)):
        Veclist.append(setofWordsVec(vocablist,data[i]))
    Veclist = np.array(Veclist)
    print(Veclist)
    p0vect,p1vect,pAbusive = train_model(Veclist,target)
    testentry = [['love','my','dalmation'],
                 ['stupid','garbage'],
                 ['love']]
    testlist = []
    lentestentry = len(testentry)
    for j in range(lentestentry):
        testlist.append(setofWordsVec(vocablist,testentry[j]))
    testveclist = np.array(testlist)
    pre = []
    for k in range(lentestentry):
        pre.append(pre_classify(testveclist[k],p0vect,p1vect,pAbusive))
    pre = np.array(pre).reshape(lentestentry,1)
    print(pre)

