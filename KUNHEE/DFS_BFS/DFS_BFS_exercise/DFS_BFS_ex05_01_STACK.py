#stack : 한쪽에서 데이터를 넣고 빼는 자료구조
#queue : 한쪽에서 데이터를 넣고 반대쪽에서 빼는 자료구조
#data structure
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)
print(stack[::-1])