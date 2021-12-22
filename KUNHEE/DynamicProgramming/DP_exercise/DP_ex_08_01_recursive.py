# Chapter8 Dynamic Programming(동적 계획법)
# 메모리 공간을 약간 더 사용하여 연산 속도를 비약적으로 증가시킨다.

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))
