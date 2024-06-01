import sys
import time

not_lst = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=',
           'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\',
           'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', "'",
           'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/', ' ']

org_lst = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-',
           'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']',
           'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';',
           'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', ' ']

try:
    while True:
        line = input() 
        lst = list(line)
        for char in lst:
            if char in not_lst:
                k = not_lst.index(char)
                print(org_lst[k], end='')
        print()
except EOFError:
    pass
