 A-list(map(int,input().split()))
 l=[]
        A = ''.join(map(str, A))

        for i in range(len(A)):
            a=A[0:i+1]
           
            g=int(a,2)
            if(g%5==0):
                l.append(True)
            else:
                l.append(False)
             
             
        return l
