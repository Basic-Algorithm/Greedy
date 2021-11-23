n = int(input())
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    
    #이해 안되는 부분
    # 입력 예시에서 U를 입력받을 때 (0,4) 좌표로 가지 않는 이유
    # 공간을 벗어나는 경우 무시
    if nx < 1 or ny <1 or nx > n or ny > n:
        continue
    
    x, y = nx, ny
    
print(x, y)