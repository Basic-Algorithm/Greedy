# split(' ')랑 split() 기능은 같을듯.
n, m = list(map(int, input().split(' ')))
array = list(map(int, input().split()))

start = 0
end = max(array)

# 이진 탐색 수행
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