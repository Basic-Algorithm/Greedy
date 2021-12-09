# def binary_search(array, target, start, end):
#     if start > end:
#         return None
    
#     # 수정해보려했지만 실패..
#     mid = (array[start] + mid[end]) // 2
#     if mid == target:
#         return mid
#     elif mid > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    


# n, m = list(map(int, input().split()))
# array = list(map(int, input().split()))

# array.sort()
# result = 0
# for i in array:
#     result += i - h
    
# if result == m:
#     print(h)
# else:
#     return None


# split(' ')랑 split() 기능은 같을듯.
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

# 어차피 start = 0해도 한 단계 차이네
start = min(array)
end = max(array)

result = 0
while(start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        if x > mid:
            total += x - mid
    # 왼쪽 이진 탐색
    if total < m:
        end = mid - 1
    # 오른쪽 이진 탐색
    else:
        result = mid
        start = mid + 1
        
print(result)