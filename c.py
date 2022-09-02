inp = int(input())
count = 0
sum = 0
while inp!=0:
    sum+=inp
    count+=1
    inp = int(input())
print(round(sum/count,2))