def setting(data):
    return data[1]

n = int(input())

array = []
# tuple형태로 리스트에 저장하기
# tuple은 (x, y)형태임.
for i in range(n):
    array.append(tuple(input().split()))

# 숫자를 기준으로 오름차순 정렬하기
result = sorted(array, key=setting)

# print(result)
#정렬된 리스트에서 tuple에서 맨처음값들을 띄어쓰기하여 출력하기
for x, y in result:
    print(x, end=' ')
