# n = int(input())
# data = list(map(int, input().split()))

# print(n)
# print(data)

# ----------------------------------------
# 책 답안 예시
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0
count = 0

for i in data:
    count += 1
    if count >= i:
        result += 1
        count = 0 # 현재 그룹의 인원수 초기화
        
print(result)