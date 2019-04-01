import random ## sonda kullanılacak
table=[] ## table                 ## global tanımlandı
tablesize=13 ## tablesize
def makeatable(tablesize):
    # ASSERT : n SHOULD BE PRIME
    for i in range(tablesize):  ## tablo 0' lar ile dolduruldu.
        table.append(0)

def my_hash(number): ## ilk başta insert_my_number fonksiyonunu oku
    return number%tablesize  ## burada nereye yerleşeceğini görmek için numarayla tablo boyunun modu alındı

def insert_my_number(number):
    Collision=False ## cakisma kontrol
    index = my_hash(number) ## indexi öğrenmek icin my_hash fonksiyonuna yollandı sayı
    if(table[index]==1): ## eğer önceden o index 1 yapılmışsa
        Collision=True   ## collision true işaretlendi
    else:
        table[index]=1 ## değilse o index 1 yapıldı
    return Collision  ## cakısma olup olmadıgı geri döndürüldü

def test():
    makeatable(table) ## tekrardan diziyi temizledim
    sayac = 0 ## sayac olusturduk kac kere collision oldugunu sayıcak
    for i in range(10):
        randomnum = random.randint(0,10000)
        if(insert_my_number == True): ## baktık collision varsa 
            sayac += 1  ## sayacı bir arttırdık.
    return sayac
print(test())  



