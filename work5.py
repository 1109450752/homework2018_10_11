import random
s1=[]
s=[0,1,2,3,4,5,6,7,8,9]
for i in range(1000):
    s1.append(random.randint(0,9))
for i in s:
    print(i,s1.count(i))

