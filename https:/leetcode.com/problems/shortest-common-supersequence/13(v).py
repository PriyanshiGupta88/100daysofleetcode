class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        X=str1
        Y=str2
        m=len(X)
        n=len(Y)
        L = [[0 for x in range(n+1)] for x in range(m+1)] 
        for i in range(m+1): 
            for j in range(n+1): 
                if i == 0 or j == 0: 
                    L[i][j] = 0
                elif X[i-1] == Y[j-1]: 
                    L[i][j] = L[i-1][j-1] + 1
                else: 
                    L[i][j] = max(L[i-1][j], L[i][j-1]) 

        
        
        lcs = "" 

        # Start from the right-most-bottom-most corner and 
        # one by one store characters in lcs[] 
        i = m 
        j = n 
        while i > 0 and j > 0: 

            # If current character in X[] and Y are same, then 
            # current character is part of LCS 
            if X[i-1] == Y[j-1]: 
                lcs+= X[i-1] 
                i-=1
                j-=1
                

            # If not same, then find the larger of two and 
            # go in the direction of larger value 
            elif L[i-1][j] > L[i][j-1]:
                lcs+=X[i-1]
                i-=1
            else:
                lcs+=Y[j-1]
                j-=1
        while i > 0:
            lcs+=(X[i - 1])
            i = i - 1
        while j > 0:
            lcs+=(Y[j - 1])
            j = j - 1
        return lcs[::-1]

