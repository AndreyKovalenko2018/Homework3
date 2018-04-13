#5
s='We are not what we should be!? We are not what, we need to be. But at least we, are not what we used to be (Football Coach)'
s=s.split()
print('Lengh:', len(s))
d=0
g=[]
for item in range(len(s)):
    f=s[d].strip(':;!,.?()')
    d=d+1
    g.append(f)
    h=' '.join(g)
print(h)
print('Sorted:', sorted(h.split(), key=str.lower))
