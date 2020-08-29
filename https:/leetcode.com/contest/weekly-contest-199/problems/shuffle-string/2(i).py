 n=input()
 ir=list(map(int,input()))
d={}
        for i,j in zip(n,ir):
            d[j]=i
        S=""
        for i in range(len(s)):
            S+=d[i]
        return S
        
