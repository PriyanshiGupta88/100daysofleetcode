class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        lt=len(t)
        ls=len(s)
        e=0
        for i in range(len(s)):
            if s[i] in t:
                e+=1
                c=t.index(s[i])
                t=t[c+1:]
            else:
                return False
                break
        return(e==ls)
        
            
