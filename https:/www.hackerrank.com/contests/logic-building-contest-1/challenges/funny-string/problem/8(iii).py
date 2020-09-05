s=input()
a=s[::-1]
    l=[]
    m=[]
    n=[]
    o=[]
    for i in range(len(s)):
        l.append(ord(s[i]))
        m.append(ord(a[i]))
    
    for i in range(1,len(s)):
        n.append(abs(m[i]-m[i-1]))
        o.append(abs(l[i]-l[i-1]))
    if(n==o):
        print(("Funny"))
    else:
        print("Not Funny")
  
