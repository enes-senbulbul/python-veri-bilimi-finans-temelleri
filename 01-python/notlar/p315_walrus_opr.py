# Standart Atama vs. Walrus Operatörü (+Python 3.8)
metin = "Matematiksel Modelleme"

uzunluk = len(metin)                    # Klasik yöntem
if uzunluk > 15:
    print(f"Klasik: Metin çok uzun ({uzunluk} karakter)")

if uzunluk_w:=len(metin) > 15:          # Walrus Operatörü ile
    print(f"Walrus: Metin çok uzun ({uzunluk} karakter)")  


# while döngüsü ile girdi alma
# Walrus operatörü dosya satır satır okunurken veya sensör verisi dinlenirken
# çok kullanılır.
veri_kuyrugu = [12.5, 14.1, 10.0, -1.0, 99.9]

def sensor_oku():
    return veri_kuyrugu.pop(0)

while (deger := sensor_oku()) >= 0:     
# deger'i iki defa çağırmıyoruz ve x2 alan kullanmanın önüne geçiyoruz.
    print("Sıcaklik Normal", deger) 


# Veri Akışı Okuma 
mesaj = "Bir işlem girin (Çıkmak için -> 'cikis'): "
while komut:=input(mesaj) != "cikis":
    print(f"Çalıştırılan işlem: {komut.upper()}")
print("Sistemden başarıyla çıkıldı.")

# Pratik - Radyan Açıları tek sefer hesapla, işlem yükünü yarıya indir.
import math
derece_aci = [10, 45, 8, 90, 15]
radyan_aci = [radyan for derece in derece_aci if (radyan:=math.radians(derece))>0.5]
print(f"Dik acilar, radyan cinsinden: {radyan_aci}")