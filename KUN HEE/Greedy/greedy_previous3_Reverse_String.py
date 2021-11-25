# s = input()

# total = len(s)
# sum_one = 0
# for i in range(total):
#     sum_one += int(s[i])
    
# sum_zero = total - sum_one
# # print(total, sum_one, sum_zero)

# if sum_one > sum_zero:
    
    
# else :
# ----> 해봤는데 반례 발견함. 01110
# ---------------------------------------------
data = input()
count0 = 0
count1 = 0

if data[0] == '1':
    count0 += 1
else:
    count1 += 1
    
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1] == '1':
            count0 += 1
        else :
            count1 += 1
            
print(min(count0, count1))

