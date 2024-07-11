def is_square(n):
    root = int(n ** 0.5)
    return root ** 2 == n

def min_square(n):
    if is_square(n):
        return 1
    
    for i in range(1, int(n ** 0.5) + 1):
        if is_square(n - i ** 2):
            return 2
    
    for i in range(1, int(n ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if is_square(n - i ** 2 - j ** 2):
                return 3
            
    return 4

n = int(input())
print(min_square(n))