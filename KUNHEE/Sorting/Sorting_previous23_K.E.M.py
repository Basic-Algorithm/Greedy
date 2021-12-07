n = int(input())
datas = []

for i in range(n):
    datas.append(tuple(input().split()))

# 우선순위로 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 사전순으로 오름차순
# datas.sort(key = lambda x : (-x[1], x[2], -x[3], x[0]), reverse=True)
# TypeError: bad operand type for unary -: 'str'
datas.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))



for data in datas:
    print(data[0], end = '\n')