#두 배열을 비교해 다른 원소의 개수를 세는 함수
def count_different_elements(array1, array2):
    count = 0
    rows = len(array1)
    cols = len(array1[0])

    for i in range(rows):
        for j in range(cols):
            if array1[i][j] != array2[i][j]:
                print(i,j, array1[i][j], array2[i][j])
                count += 1
    print(count)
    return count


n, m = map(int, input().split())

arr = []

for i in range(n):
    s = input().strip()
    row = list(s)
    arr.append(row)

    #str은 파이썬 내장 함수 이름과 같으므로 피하는 것이 좋다
    #변환한 배열은 다른 변수를 이용하여 저장-> 가독성 상승

#print(arr)


arr_WB = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'B', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]
arr_BW = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

ans = 32

for i in range(n - 7):
    for j in range(m - 7):
        sub_arr = [arr[x][j:j+8] for x in range(i, i+8)]
        
        res_a = count_different_elements(sub_arr, arr_BW)
        res_b = count_different_elements(sub_arr, arr_WB)

        ans = min(ans, res_a, res_b)
print(ans)

#not solved : 예제입력1 입력시 1이 아닌 8이 출력됨