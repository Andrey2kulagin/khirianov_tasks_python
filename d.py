in_str = input().split()
price = int(in_str[0])
delta = int(in_str[1])
m = int(in_str[2])
all_count = 0
day = 1
week = 1
while week<=m:
    week+=1
    while day<=7:
        day+=1
        all_count+=price
        price+=delta
    else: day = 1
print(all_count)