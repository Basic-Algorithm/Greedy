n, k = map(int, input().split())
A, B = list(map(int, input().split())), list(map(int, input().split()))

# A는 오름차순, B는 내림차순으로 정렬
A_sorted = sorted(A)
B_sorted = sorted(B, reverse = True)

# print(A_sorted, B_sorted)

# 바꿔치기하는데, 바꿔치기할 A의 원소랑 B의 원소 대소비교해야함.
# 최대 K번 바꿔치기하므로 K번보다 적은 횟수로 바꿔치기할 수도 있음.
for i in range(k):
    if A_sorted[i] < B_sorted[i]:
        A_sorted[i], B_sorted[i] = B_sorted[i], A_sorted[i]
    else:
        break

# 바꿔치기한 배열 A의 원소의 합을 구하자.
result = 0
for i in range(n):
    result += A_sorted[i]
    
print(result)