def hackerrankInString(s):
    a=""
    r="hackerrank"
    e=0
    for i in s:
        if a==r:
            break
        if i==r[e] and e<len(s):
            a+=i
            e+=1
    if(a=="hackerrank"):
        return("YES")
    else:
        return("NO")
print(hackerrankInString(input()))
