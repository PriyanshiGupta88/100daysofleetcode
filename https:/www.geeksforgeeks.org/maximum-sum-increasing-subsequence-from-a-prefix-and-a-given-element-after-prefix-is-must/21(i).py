def maxSumIS(arr, n,i,k): 
    max = 0
    s=[]
    for j in range(i+1):
        if(arr[j]<k):
            s.append(arr[j])
    s.append(arr[k])
    arr=s[:]
    n=len(arr)
    msis = [0 for x in range(n)] 
  
   
    for i in range(n): 
        msis[i] = arr[i] 
  
    
    for i in range(1, n): 
        for j in range(i): 
            if (arr[i] > arr[j] and
                msis[i] < msis[j] + arr[i]): 
                msis[i] = msis[j] + arr[i] 
  
     
    for i in range(n): 
        if max < msis[i]: 
            max = msis[i] 
  
    return max
a=list(map(int,input().split()))
print(maxSumIS(a,len(a),int(input()),int(input())))
