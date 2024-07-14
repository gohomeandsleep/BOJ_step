from collections import deque

def priority(n, lst):
    queue = deque(lst)
    prior = deque(range(len(lst)))
    cnt = 1

    while len(queue) > 1:
        if queue[0] == max(queue):
            if n == prior[0]:
                return cnt
            queue.popleft()
            prior.popleft()
            cnt += 1
        else:
            queue.append(queue.popleft())
            prior.append(prior.popleft())
        #print(queue, prior)
    return cnt
             
T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    print(priority(m, lst))