import math
def lis(nums):
    t=nums[:]
    t1=nums[:]
    for i in range(len(nums)):
        for j in range(i):
            if(arr[i]>arr[j] and t[i]<t[j]+arr[i]):
                t[i]=t[j]+arr[i]
    for i in range(len(nums)-2,-1,-1):
        for j in range(len(nums)-1,i,-1):
            if(arr[i]>arr[j] and t1[i]<t1[j]+arr[i]):
                t1[i]=t1[j]+arr[i]
    m=-math.inf
    for i,j,k in zip(t,t1,nums):
        m=max(m,i+j-k)
    return m
t=int(input())
for i in range(t):
    a=input()
    arr=list(map(int,input().split()))
    print(lis(arr))
    
