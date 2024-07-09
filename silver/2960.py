def sieve_of_eratosthenes(n, k):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False

    cnt = 0
    for p in range(2, n + 1):
        if is_prime[p]:
            for i in range(p, n + 1, p):
                if is_prime[i]:
                    is_prime[i] = False
                    cnt += 1
                    if cnt == k:
                        return i
    return -1 

n, k = map(int, input().split())
print(sieve_of_eratosthenes(n, k))