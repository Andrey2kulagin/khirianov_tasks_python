#на тестах выдаёт ошибку синтаксиса, хотя на локальном компьютере всё работает. Скорее всего, там старый питон
def cure_print(a: list):
    for i in a:
        print(f"{float(i[0]):.2f} {float(i[1]):.3f}")


count = int(input())
data = []
for i in range(count):
    cure_arr = input().split()
    coef_ = float(cure_arr[1]) / float(cure_arr[0])
    cure_arr.append(coef_)
    data.append(cure_arr)
data.sort(key=lambda x: x[2])
cure_print(data)
