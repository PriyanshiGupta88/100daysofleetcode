class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        s=0
        r=0
        if len(nums)==0:
            return 0
        c=nums[0]
        for i in range(1,len(nums)):
            if c<nums[i]:
                s+=1
                c=nums[i]
                r=max(r,s)
            else:
                c=nums[i]
                s=0
        return r+1
