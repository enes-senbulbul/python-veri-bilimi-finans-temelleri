# --- SCOPE RULES ---

# Global Değişkeni Okuyabilmek + Değiştirebilmek 
seviye = 1
def okuma_denemesi():
    # Localde seviye değişkeni yok, Python otomatik olarak global'e iner ve okur. 
    print(seviye)       

def degistirme_denemesi():
    # Python gövdeyi tarar ve ='li satırı gördüğü için seviye'yi fonksiyonun başından itibaren 
    # local kabul eder.
    try:
        seviye += 1     # Bu satıra gelindiğiğinde "local seviye" hala boş... Hata mesajı durumu iyi anlatıyor.
    except Exception as hata_mesaji:
        print(f"Hata yakalandı: {type(hata_mesaji).__name__} - {hata_mesaji}")

okuma_denemesi()            # Çıktı: 1
degistirme_denemesi()       # Çıktı: "Hata mesajı"

def degistirme_global():     
    global seviye           # En dıştaki global seviye'yi hedefler.
    seviye += 1
    print(seviye)           

def dis_fonksiyon():
    seviye = 100
    def ic_fonksiyon():
        nonlocal seviye     # Global seviye'yi değil bir üstteki seviye değişkenini hedefler.
        seviye += 1
        print(seviye)
    ic_fonksiyon()

degistirme_global()         # Çıktı: 2
dis_fonksiyon()             # Çıktı: 101



# --- CLOSURE RULES --- 

# state tutan fonksiyon oluşturmak
def carpan_yap(katsayi):
    def carp(x):
        return x*katsayi    # Katsayi bir free variable - Enclosing scope'tan geliyor.
    return carp

carp_1 = carpan_yap(2) # 2'yi tutan carpan_yap fonksiyonu
carp_2 = carpan_yap(3)   # 3'u tutan carpan_yap fonksiyonu
print(carp_1(5))
print(carp_2(5))

# Sıradan fonksiyon state'i unutur, closure hatırlar.
def normal_sayac():
    n = 0
    n += 1
    return n
print(normal_sayac())   # Çıktı: 1
print(normal_sayac())   # Çıktı: 1      - Her çağrıda n sıfırdan başlar

def sayac_uret():
    n = 0
    def artir():
        nonlocal n
        n += 1
        return n
    return artir

sayacim = sayac_uret()
print(sayacim())        # Çıktı: 1 
print(sayacim())        # Çıktı: 2      - Closure, n'yi hafızasında koruyor.