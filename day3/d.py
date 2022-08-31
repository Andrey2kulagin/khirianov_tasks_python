num = int(input())
out = []
for i in range(1,num):
    if i**2<=num:
        out.append(i**2)
print(*out)   