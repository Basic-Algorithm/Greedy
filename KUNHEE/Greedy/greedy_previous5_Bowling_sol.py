n, m = map(int, input().split())
data = list(map(int, input().split()))

# 원소가 0이고 길이가 11인 리스트 생성하고 볼링공의 개수 정리
# 파이썬은 0 부터 시작하니까 원소가 11개.
array = [0] * 11
for x in data:
    array[x] += 1

# 1부터 순서쌍을 구하고 원소개수 곱해주기
# 그러고 나서 1 삭제하고 2부터 반복하기
result = 0
for i in range(1, m + 1):
    n -= array[i]
    result += array[i] * n

print(result)