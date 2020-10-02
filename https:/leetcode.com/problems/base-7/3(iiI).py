num=int(input())
if num == 0:    return "0"
        s = ""
        if num < 0:
            f = -1
        else:
            f = 1
        num = abs(num)
        while num:
            s += str(num % 7)
            num //=7
                
            
        
        
        return s[::-1] if f == 1 else '-' + s[::-1]
