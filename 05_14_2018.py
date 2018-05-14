"""import time
def calc_squares(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("squares:", n*n)

def calc_cubes(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print("cubes:", n*n*n)
        
arr= [2,3,8,9]
t=time.time()
calc_squares(arr)
calc_cubes(arr)

print("done in:",time.time()-t)
print("Hah... I am done with all my work now!")"""


"""import threading
import time
exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name =  name
        self.counter = counter
    def run(self):
        print("Starting" + self.name)
        print_time(self.name, self.counter, 5)
        print("Exiting" + self.name)
        
def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)

thread1.start()
thread2.start()


thread1.join()
thread2.join()

print("Existing Main Thread")"""


"""import threading
import time
class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):        
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name =  name
        self.counter = counter
    def run(self):
        print("Starting" + self.name)
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        threadLock.release()
    def print_time(threadName, delay, counter):
        while counter:
            time.sleep(delay)
            print("%s: %s" % (threadName, time.ctime(time.time())))
            counter -= 1
    threadLock = threading.Lock()
    threads = []
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 2)
thread1.start()
thread2.start()
thread1.appened(thread1)
thread2.appened(thread2)
for t in threads:
    t.join()
    print("Exiting Main Thread")"""

class myThread(threading.Thread):
    def __init__(self, threadID, name,q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print("Starting" + self.name)
        process_data(self.name, self.q)
        print("Exiting" + self.name)

    def process_data(threadName,q):
        while not exitFlag:
            queueLock.acquire()
            if not workQueue.empty():
                data = q.get()
                queueLock.release()
                print("%s processing %s" % (threadName,ArithmeticError data))
                else:
                    queueLock.release()
                    time.sleep(1)


threadList = ["Thread-1", "Thread-2", "Thread-3"]
namelist = ["One", "Two", "Three", "Four", "Five"]
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1
for tName in threadList: 
    thread = myThread(threadID, tName, workQueue) 
    thread.start() 
    threads.append(thread) 
    threadID += 1



queueLock.acquire() 
for word in nameList: 
    workQueue.put(word) 
queueLock.release() 


while not workQueue.empty():
    pass

exitFlag = 1

for t in threads: 
    t.join() 
print ("Exiting Main Thread")


    
    
        
    






















