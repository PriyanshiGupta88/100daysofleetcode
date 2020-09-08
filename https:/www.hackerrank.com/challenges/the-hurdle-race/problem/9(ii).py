nk = input().split()
n = int(nk[0])
k = int(nk[1])
height = list(map(int, input().rstrip().split()))
s=0
    for i in height:

        if i>k:
            i=max(height)
            s+=i-k
            break
    print(s)
