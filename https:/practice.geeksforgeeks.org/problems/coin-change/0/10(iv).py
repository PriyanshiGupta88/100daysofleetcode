def count(self, nums, n, m): 
        # code here 
        t =[[0 for i in range(m+1)] for j in range(n+1)]
        for i in range(n+1):
            t[i][0] = 1

        for i in range(1,n+1):
            for j in range(1,m+1):
                if nums[i-1]<=j:
                    t[i][j] = (t[i-1][j] + t[i][j-nums[i-1]])
                else:
                    t[i][j] = t[i-1][j]
        return(t[n][m])
