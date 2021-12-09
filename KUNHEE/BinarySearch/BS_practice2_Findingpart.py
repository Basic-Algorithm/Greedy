
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return "yes"
    
    elif array[mid] > target:
        return binary_search(array, target, start, mid - 1)
    
    else:
        return binary_search(array, target, mid + 1, end)
    
n = int(input())
n_part = list(map(int, input().split()))
m = int(input())
m_part = list(map(int, input().split()))

n_part.sort()
m_part.sort()

for i in range(m):
    result = binary_search(n_part, m_part[i], 0, n - 1)
    
    if result == None:
        print("no", end = ' ')
    else:
        print(result, end = ' ')

