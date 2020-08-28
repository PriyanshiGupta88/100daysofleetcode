year,month,date=map(int,date.split('-'))
m=[0,31,28,31,30,31,30,31,31,30,31,30]
ans=0
ans+=sum(m[:month])
ans+=date
if year%4==0:
  if month>2 and year != 1900:
    ans+=1
print(ans)
