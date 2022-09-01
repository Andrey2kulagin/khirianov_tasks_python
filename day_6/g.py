#На двух последних тестах валится, вводные данные некоректные, но я считаю, что программа выводит правильный результат
def set_small_str(str, a):
    cure_str_arr = []
    cure_str = ""
    for i in range(len(str)):
        cure_str += str[i]
        step = (len(str) / abs(a))
        if ((i + 1) % step) == 0:
            cure_str_arr.append(cure_str)
            cure_str = ""
    return cure_str_arr


def is_arr_el_simmilary(arr):
    if len(arr)==0:
        return False
    for i in range(len(arr) - 1):
        if arr[i] != arr[i + 1]:
            return False
    return True


str = input()
a = int(input())
if a < 0:
    sqrt = set_small_str(str, a)
    if is_arr_el_simmilary(sqrt):
        print(sqrt[0])
    else:
        print("NO SOLUTION")
elif a > 0:
    print(str * a)
