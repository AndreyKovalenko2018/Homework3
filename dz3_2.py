#2
s = input("Enter word:")
x = len(s)//2
if len(s)%2==0:
    s = s[x:]+s[:x]
    print (s)
else:
    s= s[x+1:]+s[:x+1]
    print (s)