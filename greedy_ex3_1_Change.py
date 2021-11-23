# N = input('how much is change?:')
# int_N = int(N)
# x_500 = int_N // 500
# x_100 = (int_N-500*x_500) // 100
# x_50 = (int_N-500*x_500-100*x_100) // 50
# x_10 = (int_N-500*x_500-100*x_100-50*x_50) // 10

# P = x_500 + x_100 + x_50 + x_10
# print(P)

#--------------------------------------------------------
#better answer O(K)
n = 1260
count = 0

coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
print(count)