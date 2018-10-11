def cesi(s):
    for i in range (len(s)):
        if s[0]!=s[i]:
            return False
            break
    return True
s=[1,2,3,4]
s1=[1,1,1,1]
s2=[2,2,2]
print(cesi(s))
print(cesi(s1))
print(cesi(s2))