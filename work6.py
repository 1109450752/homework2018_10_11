def index(s):
    q=min(s)
    j=0
    for i in s:
        if i == q:
            return j
        j+=1
s=[2,3,4,6,2,3,1,7,9]
print(index(s))