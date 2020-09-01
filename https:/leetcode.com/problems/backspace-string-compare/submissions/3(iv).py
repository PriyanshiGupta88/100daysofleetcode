 S=input()
 T=input()
 s=[]
        l=[]
        for i in S:
            if i!="#":
                s.append(i)
            else:
                if len(s)>=1:
                    s.pop(-1)
        for i in T:
            if i!="#":
                l.append(i)
            else:
                if len(l)>=1:
                    l.pop(-1)
        return(s==l)
                                 
