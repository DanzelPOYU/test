n=int(input())
a=1
b=1
i=2
c=0
if i>=n:
    print(1)
else:
    while i<n:
        c=a+b
        a,b=b,c
        i+=1
    print(c,end = ' ')