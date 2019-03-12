def recMC(coinValueList,change):
    mincoins=change
    if(change in coinValueList):
        return 1
    else:
        for i in [c for c in coinValueList if c<=change]:##expression
            numberofcoins = 1+recMC(coinValueList,change-i)
            if numberofcoins < mincoins:
             mincoins = numberofcoins
    return mincoins
list1=[1,5,10]
print(recMC(list1,111))
