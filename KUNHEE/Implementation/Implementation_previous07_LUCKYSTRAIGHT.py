n = str(input())

length_n = len(n)
index_middle = int(length_n / 2)
sum_left = 0
sum_right = 0
sum_total = 0

for i in range(0, index_middle):
    sum_left += int(n[i])

for i in n:
    sum_total += int(i)
sum_right = sum_total - sum_left


if sum_left == sum_right:
    print('LUCKY')
else :
    print('READY')
