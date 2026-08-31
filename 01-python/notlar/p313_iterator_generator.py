import sys                      # getsizeof fonksiyonu için

# Iterators 
sayilar = [10, 20, 30]          # Liste bir iterable'dır.
sayi_iteratoru = iter(sayilar)  # Iterable'dan iterator nesnesi oluşturduk
print(type(sayi_iteratoru))     # Çıktı: <class 'list_iterator'>

print(next(sayi_iteratoru))     # Çıktı: 10
print(next(sayi_iteratoru))     # Çıktı: 20
print(next(sayi_iteratoru))     # Çıktı: 30
# Bir daha çalıştırırsak StopIteration istisnası verir.

# Generators 
def geri_sayim(baslangic):
    sayac = baslangic
    while sayac > 0:
        yield sayac            # Değeri döndür ve burada bekle
        sayac -= -1

sayici = geri_sayim(5)          # Generator objesi oluşturur.
print(type(sayici))             # Çıktı: <class 'generator'>
print(next(sayici))             # Çıktı: 5
print(next(sayici))             # Çıktı: 4
print(next(sayici))             # Çıktı: 3


# Generator Expression
onbin_liste = [x**2 for x in range(10_000)]
onbin_generator = (x**2 for x in range(10_000))
print(f"Liste boyutu: {sys.getsizeof(onbin_liste)} byte") 
print(f"Generator boyutu: {sys.getsizeof(onbin_generator)} byte") 
# Çıktı:
# Liste boyutu: 85176 byte
# Generator boyutu: 200 byte

# Pratik
def id_uret():
    id_num = 1
    while True:
        yield id_num
        id_num += 1

kimlik_motoru = id_uret()
print("İşlem 1 ID:", next(kimlik_motoru))  # Beklenen çıktı: İşlem 1 ID: 1
print("İşlem 2 ID:", next(kimlik_motoru))  # Beklenen çıktı: İşlem 2 ID: 2 
print("İşlem 3 ID:", next(kimlik_motoru))  # Beklenen çıktı: İşlem 3 ID: 3