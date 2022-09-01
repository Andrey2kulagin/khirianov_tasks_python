n = int(input())
count = 0
i = 0
cure_count = 0
while i<n:
    inp =input()
    i+=1
    if inp =='1':
        cure_count +=1
    if cure_count>count:
         count = cure_count
    if inp =='0':
        cure_count = 0
print(count)
