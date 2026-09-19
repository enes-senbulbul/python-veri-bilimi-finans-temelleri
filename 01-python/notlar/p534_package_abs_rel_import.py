from p534_ornek_package import *
# Gelenler: PAKET_VERSIYON, Kullanici

print("-"*30)
print(f"Paket sürümü: {PAKET_VERSIYON}")

# __all__ içinde olmadığından ürünlere erişemiyoruz.
try: 
    print(f"Mevcut Ürünler: {', '.join(urun_listesini_goster())}") # type: ignore
except NameError as hata:
    print(f"Namespace'e eklenmemiş: {hata}")

# Bunu aşmanın yolu -> Absolute Import
from p534_ornek_package.urunler import urun_listesini_goster

print(f"\nŞimdi erişebiliyoruz. Mevcut Ürünler: \n{"-"*30}\n{'\n'.join(urun_listesini_goster())}")

musteri1 = Kullanici("Ali Yilmaz", bakiye=30_000)

print(f"\n{musteri1.isim} alışveriş yapmaya başlıyor. Bakiyesi: {musteri1.bakiye} TL")
print("-"*30)

musteri1.alisveris_yap(101, 1)
musteri1.alisveris_yap(103, 2)
musteri1.alisveris_yap(102, 3)

print(f"{musteri1.isim} aldıkları: {musteri1.aldiklari}")


# Çıktı: 
# [Sistem] 'p534_ornek_package' paketi yükleniyor...
# [Sistem] -> 'kullanici' alt paketi hazırlandı.
# [Sistem] -> 'islemler' alt paketi hazırlandı.
# ------------------------------
# Paket sürümü: 2.1.0
# Namespace'e eklenmemiş: name 'urun_listesini_goster' is not defined
#
# Şimdi erişebiliyoruz. Mevcut Ürünler: 
# ------------------------------
# kod:101 | Laptop | 25000 TL
# kod:102 | Mouse | 500 TL
# kod:103 | Klavye | 1500 TL

# Ali Yilmaz alışveriş yapmaya başlıyor. Bakiyesi: 30000 TL
# ------------------------------
# İşlem #1
# 1 adet Laptop sepete ekleniyor...
# Onaylandı. Ödemeniz alındı. Bakiye(Ali Yilmaz): 30000 -> 5000
# Stok (Laptop): 5 -> 4

# İşlem #2
# 2 adet Klavye sepete ekleniyor...
# Onaylandı. Ödemeniz alındı. Bakiye(Ali Yilmaz): 5000 -> 2000
# Stok (Klavye): 12 -> 10

# İşlem #3
# Ali Yilmaz <- İşlem Başarısız: Stok yetersiz :( Mouse ürününden sadece 0 tane kalmış.

# Ali Yilmaz aldıkları: ['1 x Laptop', '2 x Klavye']