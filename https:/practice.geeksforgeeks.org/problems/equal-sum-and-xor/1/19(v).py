def countValues(n):
    # Code here
    c=0
    for i in range(n):
        if((n+i)==n^i):
            c+=1
    return c
