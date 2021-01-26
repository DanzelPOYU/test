a=int(input())
b=int(input())
c=int(input())
if b%2!=0:
    x=1
else:
    x=0
if c%2!=0:
    y=1
else:
    y=0
if a%2!=0:
    z=1
else:
    z=0
d=(a//2+z)+(b//2+x)+(c//2+y)
print(d)