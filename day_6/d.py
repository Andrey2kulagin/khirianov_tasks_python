#На автотестах крашится из-за ошибки в них, там не#
inp = input()
count = 0
sum_all = 0
max = int(inp)
min = int(inp)
remains_sum = 0
troika_count = 0
troika_sum = 0
while inp!='#':
    inp = int(inp)
    troika_sum+=inp
    sum_all+=inp
    count+=1
    troika_count+=1
    if troika_count==3:
        remains_sum+=troika_sum%inp
        troika_sum=0
        troika_count=0
    if inp>max:
        max = inp
    if inp<min:
        min = inp
    inp = input()
print(round(sum_all/count,3),max,min,remains_sum)
