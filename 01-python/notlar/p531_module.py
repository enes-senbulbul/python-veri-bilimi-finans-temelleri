# Modül veya Paketi üç şekilde import edebiliriz. 

# 1) Modülü tamamen import etme - Fonksiyonlar kendi namespace'inde
import math 

sqrt = lambda x: f"{x}'in kökünü nası alim şimdi?"
print(math.sqrt(25)) 
print(sqrt(25))             # Bizim kendi namespacesimizdeki 'sqrt' ezilmedi.
# 5.0
# 25'in kökünü nası alim şimdi?


# 2) Sadece belirli nesneleri import etme - Direkt bizim global namespace'e döker.
from math import sqrt
print(sqrt(25))             # Bu sefer ezildi.
# 5.0                 


# 3) Uzun isimli modülleri 'alias' ile import etmek
import math as m
print(m.floor(5))   # Çıktı: 5 


# --- Buradan itibaren yazılan kodlar p532 için ---

def ana_uygulama():
    print("Sistem başlatıldı.")

def metin_formatla(metin: str) -> str:
    return metin.strip().lower().capitalize()

bilgiler = {
    "ad": "Ali",
    "yaş": 34,
    "sigorta": True  
}

# Bu dosyadaki fonksiyonlar modül olarak import edildiğinde aşağıdaki kodlar çalışmaz.       __name__ = dosya_adı
# Sadece direkt script olarak çalıştırıldığında çalışır.                                     __name__ = __main__
if __name__ == "__main__":

    ana_uygulama()
    metin_bilgisi = input("Metin giriniz: ")
    duzeltilmis = metin_formatla(metin_bilgisi)
    print("Düzeltilmiş hali:", duzeltilmis)