def set_empty_arr(m):
    a = []
    for i in range(m):
        a.append("")
    return a


N = int(input())
paint_data = []
cure_paint_data = []
board_numbers = []
for i in range(N * 3):
    cure_paint_data.append(int(input()))
    if len(cure_paint_data) == 3:
        paint_data.append(cure_paint_data)
        cure_paint_data = []
M = int(input())
color_array = set_empty_arr(M)
for i in range(M):
    board_numbers.append(int(input()))
for i in range(len(board_numbers)):
    flag = 0
    for j in paint_data:
        if j[0] <= board_numbers[i] <= j[1]:
            flag = 1
            color_array[i] = j[2]
    if flag == 0:
        color_array[i] = 0

print(*color_array)
