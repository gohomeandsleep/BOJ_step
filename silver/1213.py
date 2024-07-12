from collections import Counter
counter = Counter(input())
print(counter)
half_palindrome = []
odd_char = ''

for char, count in counter.items():
    if count % 2 == 1:
        if odd_char:
            print("I'm Sorry Hansoo")
            exit()
        odd_char = char
    half_palindrome.extend([char] * (count // 2))

# 결과 조합
half_palindrome.sort()
print(''.join(half_palindrome) + odd_char + ''.join(reversed(half_palindrome)))