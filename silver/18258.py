from collections import deque
import sys

class Queue:
    def __init__(self):
        self.items = deque()
    
    def enqueue(self, item):
        self.items.append(item)
    
    def is_empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.popleft()
        else:
            return -1    
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return -1
    
    def back(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return -1

n = int(input())
inst = [sys.stdin.readline().split() for _ in range(n)]
queue = Queue()

for i in range(n):
    if inst[i][0] == 'push':
        queue.enqueue(inst[i][1])
    elif inst[i][0] == 'pop':
        print(queue.dequeue())
    elif inst[i][0] == 'size':
        print(queue.size())
    elif inst[i][0] == 'empty':
        print(queue.is_empty())
    elif inst[i][0] == 'front':
        print(queue.front())
    elif inst[i][0] == 'back':
        print(queue.back())