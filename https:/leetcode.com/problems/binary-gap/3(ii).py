 N=int(input())
 s=bin(N)[2:]
        c=0
        if "1" in s:
            b=s.index("1")

            for i in range(b+1,len(s)):
                if(s[i]=="1"):
                    c=(max(c,(i-b)))
                    b=i

            return c

        else:
            return 0

