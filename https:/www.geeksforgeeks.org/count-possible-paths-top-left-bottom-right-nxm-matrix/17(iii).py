#code
def aa(r,c):
    t=[[1 for i in range(c)] 
                        for j in range(r)]
    for i in range(1,r):
        for j in range(1,c):
            t[i][j]=t[i-1][j]+t[i][j-1]
    return t[r-1][-1]%((10**9)+7)
for i in range(int(input())):
    r,c=input().split()
    print(aa(int(r),int(c)))
