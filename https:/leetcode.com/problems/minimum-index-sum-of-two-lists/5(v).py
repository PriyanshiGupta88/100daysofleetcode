class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        d={}
        o=[]
        for i in list1:
            if i in list2:
                d[i]=list1.index(i)+list2.index(i)
        v=list(d.values())
        if(len(v)>0):
            j=(min(v))
            for i in list(d.keys()):
                if(d[i]==j):
                    o.append(i)

            
            return o
        else:
            return []
        
