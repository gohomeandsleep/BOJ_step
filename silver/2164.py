from collections import deque

def find_last_person(n):
    dq = deque(range(1, n + 1))
    
    while len(dq) > 1:
        dq.popleft()
        dq.append(dq.popleft())
    
    return dq[0]

n = int(input())
last_person = find_last_person(n)
print(last_person)