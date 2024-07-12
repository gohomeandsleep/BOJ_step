from collections import deque

def func(n):
    queue = deque([(n, 0)])
    visited = set([n])

    while queue:
        current, steps = queue.popleft()
        if current == 1:
            return steps
        
        if current -1 > 0 and current -1 not in visited:
            queue.append((current -1, steps + 1))
            visited.add(current -1)
        
        if current % 2 == 0 and current // 2 not in visited:
            queue.append((current // 2, steps + 1))
            visited.add(current // 2)
        
        if current % 3 == 0 and current // 3 not in visited:
            queue.append((current // 3, steps + 1))
            visited.add(current // 3)
        #print(queue)

n = int(input())
print(func(n))