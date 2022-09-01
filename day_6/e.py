#На автотестах крашится из-за ошибки в них, там не#
def set_empty_arr(n):
    a = []
    for i in range(int(n)):
        a.append([])
    return a


def arr_normilize(array, n):
    a = []
    for i in range(n):
        if array[i]:
            array[i].sort(reverse=True)
            a.append(array[i])
    return a

def set_arrays():
    a = input()
    all_arr = set_empty_arr(a)
    for i in range(int(a)):
        all_arr.append([])
    inp1 = input()
    while inp1 != '#':
        inp = inp1.split(" ")
        all_arr[int(inp[0])].append(int(inp[1]))
        inp1 = input()
    ret_arr = arr_normilize(all_arr,int(a))
    return ret_arr


a = set_arrays()
a.sort(key=lambda x: sum(x), reverse=True)
for i in a:
    print(*i, end=" ")
