from collections import deque
class Queue:
    def __init__(self):
        self.array=deque()
    def enqueue(self,data):
        return self.array.append(data)
        rint("elements in queue is",self.array)
    def dequeue(self):
        return self.array.popleft()
    def front(self):
        return self.array[0]
    def rear(self):
        return self.array[-1]
    def length(self):
        return len(self.array)
    def print(self):
        return self.array
queue=Queue()
queue.enqueue(2)
queue.enqueue(9)
queue.dequeue()
queue.front()
queue.print()