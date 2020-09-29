def check(n):
  co=0
  ce=0
  while(n!=0):
    if(n%2!=0):
      ce+=1
    else:
      co+=1
    n=n>>2
print(co^ce)
n=int(input())
check(n)
