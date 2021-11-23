# data = list(map(str, input().split()))
            
# print(data)

# ---------------------------------------
# 책 답안 예시
data = input()

#string indexing
result = int(data[0])

#data length
for i in range(1, len(data)): 
    num = int(data[i])
    if result <= 1 or num <= 1:
        result += num
    else:
        result *= num
        
print(result)