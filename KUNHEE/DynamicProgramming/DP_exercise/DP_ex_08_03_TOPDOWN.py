d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

print(pibo(6))

#pibo(2) + pibo(1) 연산할 때, pibo(2)에서 return 1 되야하는 것 아닌가?