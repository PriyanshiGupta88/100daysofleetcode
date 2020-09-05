l=[]
    c=0
    for i in range(1,len(s)):
        if s[i].isupper():
            l.append(s[c:i])
            c=i
    l.append(s[c:])
    return(len(l))
