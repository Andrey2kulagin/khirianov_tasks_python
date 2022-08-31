num = int(input())
count =0
a =[]
max = num
while (num != 0):
    a.append(num)
    if num>max:
        max = num
    num = int(input())
for i in a:
    if i==max:
        count+=1
print(count)
