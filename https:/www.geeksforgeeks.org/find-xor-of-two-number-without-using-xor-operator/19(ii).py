def myXOR(x, y): 
    return ((x | y) &  
            (~x | ~y)) 
  
 
x = int(input())
y = int(input())
print("XOR is" ,  
       myXOR(x, y)) 
  
