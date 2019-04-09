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
def tek_boyut_dizi(n):
    dizi = []
    for i in range(n):
        dizi.append([])
        for j in range(3):
            dizi[i].append(random.randint(0,100))
    return dizi

## kendisine aktarılan bir dizideki sayıların ortalaması ve standart sapmasını return eden foksiyonu yazın

def ortalama(dizi): ## bu kod diziinin aritmetik ortalamasını bulmak için tasarlanmıştır .
    ortalama = 0
    for i in range(len(dizi)):
        for j in range(len(dizi[i])):
            ortalama += dizi[i][j]
        return ortalama/len(dizi)

def standart_sapma(dizi,aritmetik_ortalama): ## standart sapmayı bulmak için dizinin aritmetik toplamları ve dizi lazim
    eleman_farklari = []
    eleman_farklari_kareleri = []
    eleman_farklari_toplamlari = 0
    for i in range(len(dizi)): ## for döngüsü ile elemanların ortalamaya olan uzaklıklarından oluşan bir dizi elde et.
        for j in range(len(dizi[i])):
            eleman_farklari.append(abs(aritmetik_ortalama-dizi[i][j]))
        eleman_farklari_kareleri = (fark*fark for fark in eleman_farklari) ## dizideki elemanların karelerini al
        eleman_farklari_toplamlari = sum(eleman for eleman in eleman_farklari_kareleri) # dizideki elemanların karelerin toplamlarını al
    return pow((eleman_farklari_toplamlari/len(dizi)-1),1/2) ## son olarak elemankareleri toplamlarını dizinin bir azına böl ve karekökünü al

dizi = tek_boyut_dizi(10)

standart_sapma(dizi,ortalama(dizi))


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
 ##



