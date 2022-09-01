def set_result_arrays():
    a = input()
    inp1 = input()
    cure_arr = []
    student = inp1[0]
    all_arr = []
    while inp1!='#':
        inp = inp1.split(" ")
        if inp[0]!=student:
            student = inp[0]
            all_arr.append(cure_arr)
            cure_arr = [] 
        cure_arr.append(int(inp[1]))
        inp1 = input()
    all_arr.append(cure_arr)
    all_arr.sort()
    return all_arr
a = set_result_arrays()
a.sort(key=lambda x: sum(x))
print(*a)
