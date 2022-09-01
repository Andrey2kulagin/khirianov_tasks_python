in_str = input()
if in_str!='0':
    in_arr = in_str.split(" ")
    sum = int(in_arr[0])
    percent = int(in_arr[1])
    purpose = int(in_arr[2])
    year = 0
    while sum < purpose:
        sum+=sum*percent/100//0.01/100
        year+=1
    print(year)
else: print(0)