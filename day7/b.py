a = int(input())
b = int(input())
c = int(input())
if (a+b) >c and (b+c)>a and (c+a)>b:
    a = a**2
    b = b**2
    c = c**2
    if c == (a+b) or b == (a+c) or a == (c+b):
        print("right")
    elif c > (a+b)or b > (a+c) or a > (c+b):
        print("obtuse")
    elif c < (a+b) or b < (a+c) or a < (c+b):
        print("acute")
else: print("impossible") 