l=[s[0]]
    for i in range(1,len(s)):
        if( len(l)>0 and l[-1]==s[i]):
            l.pop()
        else:
            l.append(s[i])
    s=("".join(l))
    if(len(s)>1):
        return s
    else:
        return "Empty String"
