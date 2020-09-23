class Solution:
    def numTrees(self, n: int) -> int:
        def bi(n,k):
            if (k > n - k):
                k = n - k
 
            r=1
            for i in range(k):
                r=r*(n-i)
                r=r//(i+1)
            return r
        c=bi(2*n,n)
        return(c//(n+1))
        
