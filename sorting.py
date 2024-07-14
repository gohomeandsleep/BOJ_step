"""
정렬 알고리즘
1. 버블 정렬 - 인접한 두 요소를 확인하고 교환
2. 선택 정렬 - 가장 작은 요소를 찾아 교환
3. 삽입 정렬 - 이미 정렬된 부분과 비교하며 삽입
4. 병합 정렬 - 리스트를 반으로 나누고 정렬 후 병합
5. 퀵 정렬 - pivot 기준으로 작은 것은 왼쪽, 큰 것은 오른쪽
6. 힙 정렬 - 이진 트리 형태인 힙 구조로 정렬(Heapify)
"""
def bubble_sort(lst):
    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

def selection_sort(lst):
    for i in range(len(lst)):
        min = i
        for j in range(i+1, len(lst)):
            if lst[j] < lst[min]:
                min = j
        lst[i], lst[min] = lst[min], lst[i]
    return lst

def insection_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = key
    return lst

import random

org_lst = [i+1 for i in range(100)]  
lst = [i+1 for i in range(100)]
random.shuffle(lst)

if insection_sort(lst) == org_lst:
    print('ok')
else:
    print('not ok')
    print(insection_sort(lst), org_lst)