def findPosition(n):
        if(n and(not(n&(n-1)))):
            p=1
            m=1
            while(not(n&m)):
                m=m<<1
                p+=1
            return(p)
        else:
            return(-1)
n=int(input())
print(findPosition(n))
