# Geleneksel (try/finally) vs. Modern (with) Kaynak Yöneticisi 

# Eski Yol - Uzun, unutulmaya veya hata yapmaya açık.
dosya1 = open("notlar/p513_try_finally.txt", "w")
try: 
    dosya1.write("Gecici veri")
finally:
    dosya1.close()          # finally -> hata olsa da olmasa da kapat.


# Modern Yol -  with bloğu: arka planda __enter__ ve __exit__ metotları çalışır.
with open("notlar/p513_with.txt", "w") as dosya2:
    dosya2.write("Gecici veri")
    # Blok bittiği an dosya2.close() tamamen otomatik çağrılır. 


# Kendi özel Context Manager sınıfımızı tanımlayarak dunder metotları enter ve exit'in nasıl 
# çalıştığını ve edge case yakalama yeteneğini test etme
class Zamanlayici:
    def __enter__(self):
        print("Zamanlayıcı başladı (Kaynak ayrıldı)")
        return self     # 'as' kelimesinden sonra yazdığımız değişkene (dosya2) atanır.

    def __exit__(self, exc_type, exc_val, traceback):

        # exc_type: Eğer blok içinde hata çıkarsa oluşan hatanın tipini (sınıf türünü) tutar. 
        # exc_val: Oluşan hatanın nesnesini ve hata mesajını tutar.
        # traceback(exc_tb): Oluşan hatanın kodun tam olarak neresinde gerçekleştiğini gösteren traceback (izleme)
        # nesnesidir.

        if exc_type:        # Eğer hata çıkarsa
            print(f"Hata yakalandı: {exc_type.__name__}, ama kaynak 'güvenle' temizlendi.")
            return True     # True döndürerek hatayı yutarız. Programın çökmesini engelleriz.
        print("Zamanlayıcı bitti (Kaynak temizlendi)")


with Zamanlayici() as zamanlayici1:
    print("İşlem yapılıyor...")

# Zamanlayıcı başladı (Kaynak ayrıldı)  -> __enter__
# İşlem yapılıyor...
# Zamanlayıcı bitti (Kaynak temizlendi) -> __exit__

with Zamanlayici() as zamanlayici2:
    print("Riskli işlem yapılıyor...")
    raise ValueError("Beklenmeyen çökme!")     # Program çökmeyecek, '__exit__' kurtaracak.

# Zamanlayıcı başladı (Kaynak ayrıldı)
# Riskli işlem yapılıyor...
# Hata yakalandı: ValueError, ama kaynak 'güvenle' temizlendi.

# --------------------------------------------------------
# ValueError                                    exc_type
# ValueError('Beklenmeyen çökme!')              exc_val
# <traceback object at 0x0000...>               exc_tb