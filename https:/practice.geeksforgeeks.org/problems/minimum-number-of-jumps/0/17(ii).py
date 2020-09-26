""
import math
def minjumps(arr,n):
    ju=[0 for i in range(n)]
    if n==0 or arr[0]==0:
        return (-1)
    for i in range(1,n):
        ju[i]=math.inf
        for j in range(i):
            if(i<=j+arr[j]) and (ju[j]!=math.inf):
                ju[i]=ju[j]+1
                break
        #print(ju)
    #print(ju)
    if ju[n-1]!=math.inf:
        return ju[n-1]
    else:
        return -1
t=int(input())
for i in range(t):
    e=int(input())
    arr=list(map(int,input().split()))
    n=len(arr)
    print(minjumps(arr,n))
