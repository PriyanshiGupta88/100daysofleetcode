class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        r=S
        k=sum(nums)
        if (k+r)%2!=0: 
            return 0
        elif(k<S):
            
                return 0
        else:   
            p=(k+r)//2

            t =[[0 for i in range(p+1)] for j in range(n+1)]
            for i in range(n+1):
                t[i][0] = 1

            for i in range(1,n+1):
                for j in range(1,p+1):
                    if(nums[i-1]==0):
                        t[i][j]=t[i-1][j]
                    elif nums[i-1]<=j :
                        t[i][j] = (t[i-1][j] + t[i-1][j-nums[i-1]])
                    
                    else:
                        t[i][j] = t[i-1][j]
            
                    #print(t[n][p])
            return(t[n][p])*(2**nums.count(0))
