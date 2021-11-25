# n = int(input())
# coins = list(map(int, input().split()))

# coins.sort()

# if coins[0] !== 1:
#     result = 1
    
# print(result)

# -----------------------------------------
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

target = 1
for x in coins:
    if target < x:
        break
    target += x
    
print(target)
