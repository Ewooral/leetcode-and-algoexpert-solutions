from multiprocessing import Queue

customQueue = Queue(maxsize= 3)

customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

print(customQueue.get())
