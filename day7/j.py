N = int(input())
paint_data = []
cure_paint_data = []
board_numbers = []
color_array = []
for i in range(N*3):
    cure_paint_data.append(int(input()))
    if len(cure_paint_data)==3:
        paint_data.append(cure_paint_data)
        cure_paint_data = []
M = int(input())
for i in range(M):
    board_numbers.append(int(input()))
print(paint_data)
print(board_numbers)

