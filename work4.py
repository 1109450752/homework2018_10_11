def averagenum(num):
    nsum = 0
    for i in range(len(num)):
        nsum += num[i]
    return nsum / len(num)
s="12 34 45 56 78 12 3 44 56"
s=s.split()
s=[int(x) for x in s]
q=averagenum(s)
print(s)
print(q)
max_number=0
min_number=0
for i in s:
    if i>=q:
        max_number+=1
    else:
        min_number+=1
print(max_number,min_number)