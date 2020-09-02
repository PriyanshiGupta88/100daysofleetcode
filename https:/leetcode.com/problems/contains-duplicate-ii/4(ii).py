nums=list(map(int,input().split()))
if(len(nums)==len(set(nums))):
            return False
        for i in range(len(nums)):
            if(i<i+k+1):
                f=nums[i+1:i+k+1]
                if(nums[i] in f):
                    return True
        return False
