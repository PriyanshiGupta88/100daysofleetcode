def marsExploration(s):
    e=len(s)//3
    a="SOS"*e
    c=0
    for i,j in zip(a,s):
        if(i!=j):
            c+=1
    return(c)
s=input()
print(marsExploration(s))
