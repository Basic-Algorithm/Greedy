position = input()
column = int(ord(position[0])) - int(ord('a')) + 1
row = int(position[1])



cnt = 0
cases = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]
for case in cases:
    new_column = column + case[0]
    new_row = row + case[1]
    
    if 1 <= new_row <= 8 and 1 <= new_column <= 8:
        cnt += 1
    
    else :
        continue


print(cnt)