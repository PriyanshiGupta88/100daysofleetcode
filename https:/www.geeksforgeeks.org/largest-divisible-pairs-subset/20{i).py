arr=list(map(int,input().split()))
n=len(arr)
d = [[0 for i in range(n)] for j in range(n)] 
q=sorted(arr)[::-1]
for i in range(n):
    for j in range(n):
        if(q[j]%arr[i]==0):
            
            if(i==0):
                d[i][j]=1
            else:
                d[i][j]=d[i-1][j]+1
        else:
            if(i!=0):
                d[i][j]=d[i-1][j]

print(max(d[n-2]))
