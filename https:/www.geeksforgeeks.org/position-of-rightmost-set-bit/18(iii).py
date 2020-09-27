#code
t=int(input())
for i in range(t):
    a=int(input())
    if a==0:
        print(0)
    else:
        p=1
        m=1
        while(not(a&m)):
            m=m<<1
            p+=1
            
        print(p)
