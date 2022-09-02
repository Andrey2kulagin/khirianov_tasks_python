#последний тест не проходился из-за большого размера файла, поэтому массив режется на маленькие по 300 элементов+-
inp = int(input())
arr = []
cure_max = inp
while inp!=0:
    arr.append(inp)
    if len(arr)>300:
        cure_cure_max = max(arr[0:-5])
        if cure_cure_max>cure_max:
            cure_max = cure_cure_max
        arr = arr[-5::]
    inp = int(input())
print(max(cure_max,max(arr[0:-5])))