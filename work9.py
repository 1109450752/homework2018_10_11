s=[1,1,3,4,4,5,7,9,10,30,11]
s1=[1,1,3,4,4,5,7,9,10,30]
def isSorted(s):
    s1=sorted(s)
    if s1==s:
        return True
    else:
        return False
print(isSorted(s))
print(isSorted(s1))
