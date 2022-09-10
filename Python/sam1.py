y,m,d = input().split()
y=int(y)
m=int(m)
d=int(d)

if m<3:
    m+=12
    y-=1
    
    a=2*m +int((6*(m+1)))/10
    b=y+y/4 -int((y/100)) + int(y/400)
    
    f1=(d+a+b+1)
    f=f1%7
    print(int(f))
    
else:
     a=2*m +int((6*(m+1)))/10
     b = y+y/4 - int((y/100)) + int(y/400)
    
     f1=(d+a+b+1)
     f=f1%7
     print(int(f))
 