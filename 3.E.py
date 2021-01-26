x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
if (x1+y1)%2==0:
    if (x2+y2)%2==0:
        print("Yes")
    else :
        print("No")
elif (x1+y1)%2!=0:
    if (x2+y2)%2!=0:
        print("Yes")
    else :
        print("No")