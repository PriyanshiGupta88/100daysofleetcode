#code
t=int(input())
for i in range(t):
    a,b=input().split()
    a=int(a)
    b=int(b)
    c=a^b
    s=0
    while(c):
        c=c&(c-1)
        s+=1
    print(s)
