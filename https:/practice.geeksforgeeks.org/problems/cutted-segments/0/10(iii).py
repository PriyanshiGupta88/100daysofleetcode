import math
def count(a,s):
    dp=[0]+[(-math.inf) for i in range(s)]
    for i in range(1,s+1):
        for r in a:
            if(i-r>=0):
                dp[i]=max(dp[i],dp[i-r]+1)
    return dp[-1]

t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    print(count(a,n))
