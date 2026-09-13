from functools import reduce 

# lambda fonksiyonu ifadesi 
kare_al = lambda x: x**2        
print(kare_al(5))           # Çıktı: 25

topla = lambda x,y: x+y     # Birden fazla parametre alan lambda fonksiyonu
print(topla(5, 21))         # Çıktı: 26
# Tabiki de değişkene atamak yanlış. İsim vermeden direkt başka bir fonksiyon içinde 
# tek seferlik kullanmamız için varlar
 

# lambda + map, filter ve reduce fonksiyonları 
sayilar = [1, 2, 3, 4, 5, 6]
kareler = list(map(lambda x:x**2, sayilar))
print("Kareler:", kareler)
ciftler = list(filter(lambda x:x%2==0, sayilar))
print("Çiftler:", ciftler)
# kareler ve ciftler'in tek kullanımlık iterator değil liste olmasını istediğimiz
# için list() kullanıyoruz. Yoksa tek bir kez kullandıktan sonra boş liste döndürürler.

liste_toplam = reduce(lambda acc, x: acc+x, sayilar, 0)
print("Listedeki elemanların toplamı:", liste_toplam)
liste_carpim = reduce(lambda acc, x: acc*x, sayilar, 1)
print("Listedeki elemanların çarpımı:", liste_carpim)


# lambda + sorted fonksiyonu 
noktalar = [(1,2), (3,-1), (0,4)]   # tuple listesi
x_axis_yakinlik = sorted(noktalar, key=lambda demet: demet[1])  # 1. indeks y koordinatı
print("Noktalar x eksenine göre yakından uzağa:", x_axis_yakinlik)

ogrenciler = [                      # dict listesi
    {"ad": "Ali", "not": 75},
    {"ad": "Ayşe", "not": 95},
    {"ad": "Mehmet", "not": 60}
]
basari_sirasi = sorted(ogrenciler, key=lambda sozluk: sozluk["not"], reverse=True)
print("Başarı sırasına göre öğrenciler:", basari_sirasi)


# Yardımcı Built-in Fonksiyonlar
isimler = ["Ali", "Ayşe", "Mehmet", "Kadir", "Sibel", "Tuğba"]
notlar = [80, 95, 70, 45, 72, 68]

for i, isim in enumerate(isimler, start=1):     # enumerate -> index + değer
    print(i, isim)

ogrenci_liste = list(zip(isimler, notlar))      # zip -> listeleri eşleştirme 
print("Öğrenci + Notu:", ogrenci_liste)
# dict oluşturmada zip baya yardım ediyor
print(dict(zip(isimler, notlar)))

print(any(puan > 90 for puan in notlar))           # any -> en az biri True mu
print(all(puan > 50 for puan in notlar))           # all -> hepsi True mu