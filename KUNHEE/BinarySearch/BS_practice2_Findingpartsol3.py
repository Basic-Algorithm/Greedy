# 집합 자료형 이용

n = int(input())
#집합 만들기
n_part = set(map(int, input().split()))
m = int(input())
m_part = list(map(int, input().split()))

for i in m_part:
    if i in n_part:
        print("yes", end = ' ')
    else:
        print("no", end = ' ')

print(n_part)