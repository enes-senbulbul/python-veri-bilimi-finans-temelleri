class Calisan:

    sirket = "Tech A.Ş."    # Class Attribute (Sınıf Özniteliği). Sınıfa ait tüm nesneler için ortak
    calisan_sayisi = 0

    def __init__(self, isim, maas):
        self.isim = isim    # Instance Attribute (Nesne Özniteliği). Her nesnenin kendi kopyası vardır.
        self.maas = maas    
        Calisan.calisan_sayisi += 1

    def zam_yap(self, oran):                # Instance Method
        self.maas += self.maas * oran
        return self.maas 

    @classmethod    
    def sirket_degistir(cls, yeni_isim):    # Class Method 
        cls.sirket = yeni_isim
        return cls.sirket

    @staticmethod 
    def maas_gecerli_mi(maas):              # Static Method -> self veya cls üzerinde çalışmaz.
        return maas >= 33_030.00            # Sadece dışarıdan gelen veriyi işler.


calisan1 = Calisan("Ali", 40_000)   
calisan1.zam_yap(0.10)      # Yine nesnelerin özniteliklerine ve methodlarına "." operatörü ile erişiyoruz.
print(calisan1.maas)                # Çıktı: 44000.0

calisan2 = Calisan("Zeynep", 42_000)
calisan2.zam_yap(0.05)
print(calisan2.maas)                # Çıktı: 44100.0

Calisan.sirket_degistir("Global Tech")
calisan1.sirket = "ABC Tech"        # Class attribute'unu nesne üzerinden değiştirirsek o nesneye ait sınıfı
print(Calisan.sirket)               # ... override eden öznitelik oluşturur.
print(calisan1.sirket)              # Sadece bunun çıktısı "ABC Tech" olur.
print(calisan2.sirket)              # Kötü pratik. Class attributelarına nesne üzerinden erişmemeliyiz.

gecerli = Calisan.maas_gecerli_mi(30_000)   # Statik metot çağrısı
print(gecerli)                              # Çıktı: False