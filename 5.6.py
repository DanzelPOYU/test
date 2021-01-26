s=input()
if s.find('p')==-1:
    print(-2)
else:
    print(s.find('p',s.find('p')+1))