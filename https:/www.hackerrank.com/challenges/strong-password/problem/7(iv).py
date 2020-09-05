s=password
r="!@#$%^&*()-+"
c=0
if (not(any(x.isdigit() for x in s))):
  c+=1
if(not(any(x.islower() for x in s))):
  c+=1
if(not(any(x.isupper() for x in s))):
  c+=1
if(not(any(x in r for x in s))):
  c+=1
if (c+n)<6:
  return(6-n)
else:
  return c
