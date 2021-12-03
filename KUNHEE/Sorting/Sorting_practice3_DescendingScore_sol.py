n = int(input())

array = []
# tuple형태로 리스트에 저장하기
# tuple은 (x, y)형태임.
for i in range(n):
    input_data = input().split()
    # print(input_data) input_data는 리스트임.
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    array.append((input_data[0], int(input_data[1])))

# key를 이용하여 점수를 기준으로 정렬
# lambda 는 함수를 정의하지 않고 간단하게 사용할 수 있게 만들어줌. 형식은 lambda x: f(x)(인자)
# lambda의 변수 student는 dummy 변수이므로 x든 y든 상관없음.
array = sorted(array, key=lambda student: student[1])
# print(array)


#정렬이 수행된 결과를 출력
for student in array:
    print(student[0], end=' ')
