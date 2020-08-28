 strs=input().split()
 if len(strs)<1:
            return ""
        strs.sort()
        a=strs[0]
        b=strs[-1]
        s=""
        for i,j in zip(a,b) :
            if(i==j):
                s+=i
            else:
                break
        return s
