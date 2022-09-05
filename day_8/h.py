a = [32, 52, 1,]
Flag = False
while not Flag:
    Flag = True
    for i in range(len(a) - 1):
        if len(str(a[i])) == len(str(a[i + 1])):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                Flag = False
        else:
            min_len = min(len(str(a[i])),len(str(a[i+1])))
            cure_a = str(a[i])[-1::]
            cure_a_i = str(a[i+1])[-1::]
            for i in range(min_len):
                if int(cure_a_i[i])>int(cure_a[i]):
                    a[i], a[i + 1] = a[i + 1], a[i]
                    Flag = False
print(*a)
