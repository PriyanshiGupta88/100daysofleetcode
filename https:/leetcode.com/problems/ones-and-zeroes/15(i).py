"""import numpy as np
class Solution:
    def findMaxForm(self, a: List[str], m: int, n: int) -> int:
        dp = [[0] * (n+1)  for _ in range(m+1)]        
        for i in range(len(a)):
            c = Counter(a[i])
            for j in range(m+1)[::-1]:
                for k in range(n+1)[::-1]:                                        
                    dp[j][k] = max(dp[j][k], dp[j-c['0']][k-c['1']] + 1 if c['0'] <= j and c['1'] <= k else 0)                                 
        return dp[m][n]
"""
import numpy as np
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [ [0]*(n+1) for _ in range(m+1) ]   # [0][1]
        
        for ones, zeros in [ (s.count('1'), s.count('0')) for s in strs]:
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max([ dp[i][j], dp[i-zeros][j-ones]+1 ])

        return dp[m][n]
