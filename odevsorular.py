import random
Matris = [[3,2,1],[0,0,0],[0,0,0]]
Matris_2  = [[3,1,7],[1,26,7],[3,1,9]]

## odev1.txt dosyası kullanılmıştır
## odev1.txt dosyasının içinde " Emir Ali Kıvrak" yazmaktadır.
f = open("odev1.txt","r") ## kelime okundu
my_word_list = f.read() ## kelime my_word_lise atıldı
def trueorfalse(text,kelime): ## fonskiyon içine text ve kelime aldı
    dizi = text.split() ## textin her elemanı ayrıldı ve diziye atıldı
    for i in dizi:
        if(i == kelime): ## eğer aranan içerde varsa true döndü
            return True
    else: ## yoksa false döndü
        return False

def trueorfalseall(text,my_string): ## fonksiyon text içinde aratılanı bulur kelime olmasına gerek yok hece olsa da bulur.
    uzunluk = len(text)
    for i in range (uzunluk):
        for j in range(uzunluk,-1,-1):
           if(text[i:j]==my_string):
            return True
    return False
print(trueorfalseall(my_word_list,"Emi"))
print(trueorfalse(my_word_list,"Emir"))

def pandigital(kelime): ## girilen string terside aynıysa True veirir örnek kabak --> true araba-->false
    if(kelime == kelime[::-1]):
        return True
    return False

print(pandigital("araba"))

def tek_boyut_olustur(eleman_sayisi): ## girilen eleman sayisi kadar random tek boyutlu dizi oluşturur
    dizi = []
    for i in range(eleman_sayisi):
        dizi.append(random.randint(1,3))
    return dizi

def doldur(row,colomun,dizi): ## tek boyutlu dizi alır ve iki boyutlu diziye doldurur.
    two_dimensional_array = []
    sayac = 0
    for i in range(row):
        two_dimensional_array.append([])
        for j in range(colomun):
            two_dimensional_array[i].append(dizi[sayac])
            sayac = sayac+1
    return two_dimensional_array

def matrisbas(matris): ## matrisi biçimlice basar
    for i in range(len(matris)):
        print(matris[i])

def satirsutunenbuyuk(dizi): ## en büyük olan satır/sutunu return eder
    enbuyuk=0
    sayac=0
    gecici=0
    for i in range(len(dizi)):
        for j in range(len(dizi[0])):
            gecici+=dizi[i][j]
            sayac+=1
        if(sayac == len(dizi[0])):
            sayac = 0
        if(gecici>enbuyuk):
            enbuyuk=gecici
        if(gecici!=0):
            gecici =0

    return enbuyuk

def kac_sifir_var(matris): ## matriste kaç sıfır olduğunu return eder
    sayac = 0
    for i in range(len(matris)):
        for j in range(len(matris[0])):
            if(matris[i][j] == 0):
                sayac+=1
    return sayac

def matris_to_hash_frequencie(matris): ## matrisi hash yapısı olan 'dictionary' ye atar. frekans şeklinde kaç elemandan kaç tane var gibi
    sayac = 0
    sayac_2 = 0
    dict={} ## hash yapısı tanımlandı
    for i in range(len(matris)):  ## 0 lar sayılacak
        for j in range(len(matris[0])):
            if (matris[i][j] == 0):
                sayac += 1
    if(sayac/len(matris)>0.3): ## eğer sıfırların sayısı %30 dan fazlaysa ife giriyor
        for i in range(len(matris)):
            for j in range(len(matris[0])):
               if(matris[i][j] in dict):
                   dict[matris[i][j]] = dict[matris[i][j]] + 1
                   sayac_2+=1
               else:
                   dict[matris[i][j]] = 1
                   sayac_2+=1
        return dict
    return 0

def matris_to_hash(matris): ## matrisi aldı
    sayac = 0 ## dictionary index'i için sayac
    sayac_2 = 0
    dict = {}
    for i in range(len(matris)):  ## 0 lar sayılacak
        for j in range(len(matris[0])):
            if (matris[i][j] == 0):
                sayac += 1
    if(sayac/len(matris)>0.3): ## eğer sıfırların sayısı %30 dan fazlaysa ife giriyor
        for i in range(len(matris)):
            for j in range(len(matris[0])):
                dict[sayac_2] = matris[i][j] #hash yapısının sayac_2.cı elemanı matrisin[i][j]. elemanına atıldı
    return dict




