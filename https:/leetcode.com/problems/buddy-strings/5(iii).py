A=input()
B=input()
if len(A)!=len(B) or len(A)<2 or len(B)<2:
            return False
        elif A==B and len(set(A))<len(A):
            return True
        S1,S2 = '',''
        for l1,l2 in zip(A,B):
            if l1!=l2:
                S1+=l1
                S2+=l2
        if len(S1)==2 and S1==S2[::-1]:
            return True
        else:
            return False
