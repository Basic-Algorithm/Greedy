n = int(input())
houses = list(map(int, input().split()))
houses.sort()

result = 0 
# n이 홀수이면 정렬했을 때 가운데 값이 설치 위치
# n이 짝수이면 정렬했을 때 가운데 두 수 중 작은 값
if n % 2 == 1:
    result = houses[n // 2]
else :
    result = houses[n // 2 - 1]
    
print(result)