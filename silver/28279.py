from collections import deque
import sys

class Queue:
    def __init__(self):
        self.items = deque()

    def push_back(self, item):
        self.items.append(item)
    
    def push_front(self, item):
        self.items.appendleft(item)
    
    def empty(self):
        if len(self.items) == 0:
            return 1
        else:
            return 0
    
    def size(self):
        return len(self.items)
    
    def print_front(self):
        if len(self.items) != 0:
            return self.items[0]
        else:
            return -1

    def print_back(self):
        if len(self.items) != 0:
            return self.items[-1]
        else:
            return -1
    
    def pop_front(self):
        if len(self.items) != 0:
            return self.items.popleft()
        else:
            return -1
        
    def pop_back(self):
        if len(self.items) != 0:
            return self.items.pop()
        else:
            return -1
        
n = int(input())
inst = [sys.stdin.readline().split() for _ in range(n)]
queue = Queue()

for i in range(n):
    if inst[i][0] == '1':
        queue.push_front(inst[i][1])
    elif inst[i][0] == '2':
        queue.push_back(inst[i][1])
    elif inst[i][0] == '3':
        print(queue.pop_front())
    elif inst[i][0] == '4':
        print(queue.pop_back())
    elif inst[i][0] == '5':
        print(queue.size())
    elif inst[i][0] == '6':
        print(queue.empty())
    elif inst[i][0] == '7':
        print(queue.print_front())
    elif inst[i][0] == '8':
        print(queue.print_back())