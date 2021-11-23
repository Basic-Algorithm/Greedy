# 어딘가 오류가 있어보인다.
# 25 5 를 입력하면 5 를 출력한다. & % 헷갈리지 말기.
n, k = map(int, input().split())

count = 0
# N이 K의 배수이면 N을 K로 나누는 과정을 수행하고 그렇지 않으면 N에서 1을 뺀다. 도중 N이 1이 되면 while 문을 빠져나간다.
while n > 1:
    if n % k == 0:
        n //= k
        count += 1
    else :
        n -= 1
        count += 1

print(count)

# -------------------------------------------
# 책 답안 예시 1
# n, k = map(int, input().split())
# result = 0

# while n >= k:
#     while n % k != 0:
#         n -= 1
#         result += 1
    
#     n //= k
#     result += 1
    
# while n > 1:
#     n -= 1
#     result += 1
    
# print(result)

#--------------------------------------------
# 책 답안 예시 2
# n, k = map(int, input().split())
# result = 0

# while True:
#     target = (n // k) * k
#     result += (n-target)
#     n = target

#     if n < k:
#         break
    
#     result += 1
#     n //= k
    
# result += (n-1)
# print(result)