a = input()
out_arr = []
for i in a:
    if i == '.':
        break
    out_arr.append(i)
out_arr.sort()
out_arr.append('.')
print(*out_arr, sep="")
