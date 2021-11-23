# 이중리스트를 만들어서 해결하려고 했음
n, m = map(int, input().split())

# 각 행을 리스트로 만들어 리스트 datas에 append하기
datas = []
for i in range(n):
    data = list(map(int, input().split()))
    datas.append(data)

# 리스트 datas에 있는 각 행의 리스트의 가장 낮은 숫자를 리스트 middle에 append하기
middle = []
for i in range(n):

    middle.append(min(datas[i-1]))

# 리스트 middle의 가장 높은 숫자 구하기
result = max(middle)
print(result)

# -------------------------------------------------
# 책 답안 예시1
# min() 함수 이용
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = min(data)
#     result = max(result, min_value)
    
# print(result)
# ----------------------------------------------------
# 책 답안 예시2
# n, m = map(int, input().split())

# result = 0
# for i in range(n):
#     data = list(map(int, input().split()))
#     min_value = 10001
#     for a in data:
#         min_value = min(min_value, a)
#     result = max(min_value, result)
    
# print(result)