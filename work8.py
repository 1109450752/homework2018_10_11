def quchong(s):
    s1=[]
    for i in s:
        if i not in s1:
            s1.append(i)
    return s1
s="1 2 3 3 1 1 4 5 7 4 6 7"
s=s.split()
s=[int(x) for x in s]
s1=quchong(s)
for i in s1:
    print(i,end=' ')
