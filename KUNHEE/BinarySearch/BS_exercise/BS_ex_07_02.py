# 이진탐색
# 배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘
# 시작점, 끝점, 중간점을 이용하여 매우 빠르게 데이터를 찾을 수 있다.

#재귀 함수로 구현

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print("원소가 존재하지 않습니다.")
    
else :
    print(result + 1)

