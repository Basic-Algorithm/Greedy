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