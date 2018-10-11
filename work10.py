def sort1(s):
    for j in range(len(s)):
        for i in range(len(s)-j-1):
            if s[i]>s[i+1]:
                t=s[i]
                s[i+1]=s[i]
                s[i]=t
s=[1,1,3,4,4,5,7,9,10,30,11]
sort1(s)
print(s)