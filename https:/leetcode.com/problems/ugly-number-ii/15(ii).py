class Solution:
    def nthUglyNumber(self, n: int) -> int:
        u=[0]*n
        u[0]=1
        i2=i3=i5=0
        m2=2
        m3=3
        m5=5
        for l in range(1,n):
            u[l]=min(m2,m3,m5)
            if u[l]==m2:
                i2+=1
                m2=u[i2]*2
            if u[l]==m3:
                i3+=1
                m3=u[i3]*3
            if u[l]==m5:
                i5+=1
                m5=u[i5]*5
        return u[-1]
