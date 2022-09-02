n = int(input())
arr = []
max_count = 0
often_simb =""
for i in range(n):
    arr.append(int(input()))
for i in arr:
    cure_count = arr.count(i)
    if cure_count >max_count:
        max_count = cure_count
        often_symb = i
print(often_symb)