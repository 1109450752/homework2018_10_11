def cesi(a,b):
    if a >= b-10:
        return 'A'
    elif a >= b-20:
        return 'B'
    elif a >= b-30:
        return 'C'
    elif a >= b-40:
        return 'D'
    else:
        return 'F'
a=input(">>")
a=a.split()
b=[int(x) for x in a]
max_mumber=max(b)
for i in b:
    s1=cesi(i,max_mumber)
    print(s1)