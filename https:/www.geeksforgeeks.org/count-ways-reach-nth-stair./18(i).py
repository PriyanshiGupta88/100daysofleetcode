#code
t=int(input())
l=[]
for i in range(t):
    a=int(input())
    l.append(a)
a=max(l) 
s=1
b=2
k=[1,2]
for i in range(a):
    c=s+b
    s=b
    b=c
    k.append(b)
for i in l:
    print(k[i-1]%(10**9+7))
    
