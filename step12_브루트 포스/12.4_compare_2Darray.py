def count_different_elements(array1, array2):
    count = 0
    rows = len(array1)
    cols = len(array1[0])  # 두 배열이 크기가 같다고 가정합니다.

    for i in range(rows):
        for j in range(cols):
            if array1[i][j] != array2[i][j]:
                count += 1

    return count

# 두 이차원 배열을 정의합니다 (크기가 같다고 가정)
array1 = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

array2 = [[1, 2, 4],
          [4, 5, 6],
          [7, 8, 9]]

# 다른 성분의 개수를 세고 출력합니다.
difference_count = count_different_elements(array1, array2)
print("다른 성분의 개수:", difference_count)