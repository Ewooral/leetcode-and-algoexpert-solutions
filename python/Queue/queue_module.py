import queue as q


mylifo = q.Queue(maxsize= 3)


print(mylifo.queue)
print(mylifo.empty())
mylifo._put(1)
mylifo._put(2)
mylifo._put(3)

print(mylifo.queue)
print(mylifo.empty())
mylifo._get()

print(mylifo.queue)
