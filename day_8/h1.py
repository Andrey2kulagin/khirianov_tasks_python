a = ["32","5","23","3"]
flag = False
while not flag:
    flag = True
    for i in range(len(a)-1):
        cure_el = a[i][::-1]
        next_el = a[i+1][::-1]
        if len(cure_el)>len(next_el):
            next_el += (len(cure_el)-len(next_el))*'0'
        else:
            cure_el+= (len(next_el)-len(cure_el))*'0'
        for j in range(len(next_el)):
            if cure_el[j]>next_el[j]:
                a[i],a[i+1]= a[i+1],a[i]
                flag = False
                break
                print(a)
print(a)
