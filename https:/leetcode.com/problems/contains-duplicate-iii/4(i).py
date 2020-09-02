nums=list(map(int,input().split()))
l=list(enumerate(nums))
        res=sorted(l,key=lambda x:x[1])
        n=len(res)
        for i in range(n-1):
            for j in range(i+1,n):
                if abs(res[j][1]-res[i][1])<=t:
                    if abs(res[j][0]-res[i][0])<=k:
                        print(True)
                else:
                    break
        print(False)
