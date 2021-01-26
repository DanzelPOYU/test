a=int(input())
if a//60>=24:
    b=a//60//24
else :
    b=a//60
print(b,a%60)