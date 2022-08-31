x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1>10 and x2>10 and y1>10 and y2>10:
    print("n/a") 
elif x1==x2:
    print("YES")
elif y1==y2:
    print("YES")
elif abs(x1-x2)==abs(y1-y2):
    print("YES")
else:
    print("NO")