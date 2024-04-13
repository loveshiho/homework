class Maker: # 定义奶茶机类，定义属性：制作速度、空闲状态、制作剩余时间
    def __init__(self,v): # 传入制作速度，单位：杯/分钟
        self.make_v = v # 制作速度
        self.currentTask = None # 空闲状态
        self.timeRemaining = 0 # 剩余时间
    def tick(self): # 定义tick方法，用于倒计时
        if self.currentTask != None:
            self.timeRemaining -= 1
        if self.timeRemaining <= 0:
            self.currentTask = None
    def busy(self): # 定义busy方法，判断制作机是否忙碌
        if self.currentTask != None:
            return True
        else:
            return False
    def startNext(self, newtask): # 定义新任务开始的方法，属性有：1 当前任务不为空，2 完成任务所需的时间
        self.currentTask = newtask
        self.timeRemaining = newtask.getCups() * 60 / self.make_v
class Task:
    def __init__(self, time):
        self.timestamp = time  # 在一小时第几秒生成制作任务
        self.cups = random.randrange(1, 6)  # 随机生成1~5杯的奶茶数
    def getStamp(self): # 定义显示任务生成所在时刻的方法，返回任务生成的时刻
        return self.timestamp
    def getCups(self): # 定义显示杯数的方法，返回当前任务中的杯数
        return self.cups # 返回当前任务中的杯数
    def waitTime(self, currenttime):  # 计算等待时间
        return currenttime - self.timestamp
def newMakerTask(is_full): # 定义新任务生成方法，若有新任务，返回True，参数传入是否高峰
    new_task = False # 初始化new_task
    if is_full:
        new_task = True
    else:
        num = random.randrange(1,181)
        if num == 180:
            new_task = True
    return new_task
def Is_full(): # 定义判断是否高峰的方法，高峰返回True
    num = random.randrange(50,551) # 生成50～551的随机数
    if num == 550: # 高峰的概率为1/500，判断是否高峰
        return True
    else:
        return False
def simulation(total_seconds, make_v):
    maker = Maker(make_v)
    makerQueue = Queue()
    waitingtimes = []
    for current_second in range(total_seconds): # 遍历整个时间轴
        is_full = Is_full() # 返回是否高峰，用is_full接收
        if newMakerTask(is_full): # 判断是否有新任务
            task = Task(current_second) # 在时间轴上标记任务
            makerQueue.enqueue(task) # 任务入列
        if (not maker.busy()) and (not makerQueue.isEmpty()): # 判断制作机的空闲状态与队列是否为空
            nexttask = makerQueue.dequeue() # 得到新任务
            waitingtimes.append(nexttask.waitTime(current_second))
            maker.startNext(nexttask) # 新任务开始，同时记录新任务属性（所花费时间等）
        maker.tick()  # 发挥制作机完成任务倒计时的作用
    avg_waitTime = sum(waitingtimes)/len(waitingtimes) # 求平均等待时间
    print("avg wait is %2.f \tsecs %3d tasks remaining." % (avg_waitTime, makerQueue.size()))
for i in range(10): # 遍历十次，根据是否高峰，改变制作速度
    make_v = 0
    if Is_full():
        make_v = 1
    else:
        make_v = 0.5
    simulation(3600,make_v)