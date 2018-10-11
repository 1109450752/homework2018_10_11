import random
s1=['1','2','3','4','5','6','7','8','9','10','J','Q','K']
s2=['red tao','red pian','black tao','black pian']
q=0
sumnumber=0
while q<4:
    q=0
    ls3 = []
    for i in range(4):
        ls=random.choice(s1)+" "+random.choice(s2)
        ls2=random.choice(s2)
        ls1=random.choice(s2)
        ls3.append(ls)
        if ls1!=ls2:
            q+=1
    sumnumber += 1
    #print(ls3)
print(ls3)
print(sumnumber)