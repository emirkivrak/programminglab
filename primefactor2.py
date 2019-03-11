import math
def primefactor(n):
    primefactors=[]
    print("asal çarpanlar")
    while n%2 == 0 :
        primefactors.append(2)
        n = n/2
    for i in range(3,int(math.sqrt(n)+1),2): 
        while n%i ==0:
            primefactors.append(i)
            n =n/i
    if n>2:
        primefactors.append(n)
    return primefactors
print(primefactor(65))
print(primefactor(20))

