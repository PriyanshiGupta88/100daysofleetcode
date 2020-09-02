arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))

c=0
        for i in arr1:
            l=[]
            for j in arr2:
                l.append(abs(i-j))
            if(all((x>d) for x in l)):
                c+=1
        return c
