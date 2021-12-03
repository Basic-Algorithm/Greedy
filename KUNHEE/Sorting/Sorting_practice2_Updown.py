n = int(input())

array = []
# 한줄씩 입력받아서 array에 저장하기
for i in range(n):
    array.append(int(input())) 

array.sort()
array.reverse()

# 리스트 출력하기
print(array)


