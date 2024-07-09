#빠른 입출력
import sys
sys.stdin.readline().rstrip()

#최대공약수 구하기(gcd)
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

#피보나치 수열
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

