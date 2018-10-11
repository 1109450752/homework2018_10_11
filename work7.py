import random
s=[2,3,4,6,2,3,1,7,9]
def daluan(s):
    s1=[]
    for i in range(len(s)):
        q=random.choice(s)
        s1.append(q)
    return s1
print(daluan(s))