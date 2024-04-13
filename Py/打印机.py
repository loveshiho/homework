from pythonds.basic.queue import Queue
import random
class Printer:
    def __init__(self, ppm):
        self.pagerate = ppm
        self.currentTask = None
        self.timeRemaining = 0
    def tick(self):
        if self.currentTask != None:
            self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.currentTask = None
    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getPages() * 60 / self.pagerate
class Task:
    def __init__(self, time):
        self.timestamp = time  # 在一小时第几秒生成打印任务
        self.pages = random.randrange(1, 21)  # 随机生成1~21页的打印页数

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currenttime):  # 计算等待时间
        return currenttime - self.timestamp


def newPrintTask():
    num = random.randrange(1, 181)
    if num == 180:
        return True
    else:
        return False


def simulation(numSeconds, pagesPerMinute):
    labprinter = Printer(pagesPerMinute)  # 传入打印速度
    printQueue = Queue()
    waitingtimes = []  # 保存每次多个任务执行时等待的时间
    for currentSecond in range(numSeconds):
        if newPrintTask():
            task = Task(currentSecond)  # 入列时间
            printQueue.enqueue(task)  # 任务入列
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.waitTime(currentSecond))
            labprinter.startNext(nexttask)
        labprinter.tick()  # 发挥倒计时的作用
    averageWait_time = sum(waitingtimes) / len(waitingtimes)
    print("avg wait is %2.f\t secs %3d tasks remaining." % (averageWait_time, printQueue.size()))


for i in range(10):
    simulation(3600, 5)
