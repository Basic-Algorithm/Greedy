#풀이1
# n, m = map(int, input().split())
# weights = list(map(int, input().split()))

# cnt = 0

# for a in weights:
#     for b in weights:
#         if a == b:
#             continue
#         else :
#             cnt += 1

## 나누기 2 하는 이유는 순서와 관계없으므로 중복 제거
# 예를 들어, 위 문제에서 (1, 2)와 (2, 1)는 같은 순서쌍.
# real_cnt = int(cnt / 2)
# print(real_cnt)


#풀이2
from itertools import product

n, m = map(int, input().split())
weights = list(map(int, input().split()))

result = list(product(weights, repeat=2))
for (a, b) in result:
    if a == b:
        result.remove((a, b))
real_result = int(len(result) / 2)
print(real_result)