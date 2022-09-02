a = int(input())
sum_ = [0,0,1]
i = 2
while sum_[i]<=a:
    cure_el = sum_[i-2]+sum_[i-1]+sum_[i]
    sum_.append(cure_el)
    i+=1
print(i)
 
    