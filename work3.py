s="2 3 4 5 66 74 33 2 3"
s=s.split()
s = [int(x) for x in s]
s1=[]
for i in s:
    if i not in s1:
        s1.append(i)
s1 = sorted(s1)
print(s1)
for i in s1:
    print(i,s.count(i))
