def lis(nums):
    t=[1]*len(nums)
    t1=[1]*len(nums)
    for i in range(1,len(nums)):
        for j in range(i):
            if(arr[i]>arr[j] and t[i]<t[j]+1):
                t[i]=t[j]+1
    for i in range(len(nums)-2,-1,-1):
        for j in range(len(nums)-1,i,-1):
            if(arr[i]>arr[j] and t1[i]<t1[j]+1):
                t1[i]=t1[j]+1
    m=t[0]+t1[0]-1
    for i in range(1,len(nums)):
        c=t[i]+t1[i]-1
        if(c>m):
            m=c
    return m
arr = [80, 60, 30, 40, 20, 10]
print ("Length of lis is", lis(arr))
