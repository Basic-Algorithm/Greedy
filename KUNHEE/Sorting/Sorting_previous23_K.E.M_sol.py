n = int(input())
students = []

for _ in range(n):
    students.append(input().split())

# 우선순위로 국어 내림차순, 영어 오름차순, 수학 내림차순, 이름 사전순으로 오름차순
students.sort(key = lambda x : (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
# TypeError: bad operand type for unary -: 'str'




for student in students:
    print(student[0])