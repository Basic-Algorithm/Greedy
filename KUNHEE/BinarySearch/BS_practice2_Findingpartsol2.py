n = int(input())
n_part = [0] * 1000001

# 부품별로 기록
for i in input().split():
    n_part[int(i)] = 1

m = int(input())
m_part = list(map(int, input().split()))

for i in m_part:
    if n_part[i] == 1:
        print("yes", end = ' ')
    else:
        print("no", end =' ')