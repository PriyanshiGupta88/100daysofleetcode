keyboards.sort()
    drives.sort()
    if(keyboards[-1]+drives[-1]<=b):
        return(keyboards[-1]+drives[-1])
    m=0
    for i in range(len(drives)-1,-1,-1):
        for j in range(len(keyboards)-1,-1,-1):
            if(drives[i]+keyboards[j]<=b):
                c=(drives[i]+keyboards[j])
                m=max(m,c)
    if(m>0):
        return m
    else:
        return -1
