class Kullanici:
    # Constructor -> Nesne oluştururken tetiklenir. 
    def __init__(self, isim, yas):      # İlk parametre 'self', Java'daki 'this'in karşılığı
        self.isim = isim                
        self.yas = yas

    def kullanici_bilgisi(self):
        print(f"Kullanıcı: {self.isim}, {self.yas}")

# Örnekleme - Instantiation / Initialization
kullanici_1 = Kullanici("Ahmet", 25)    # Python nesneyi yaratırken self'i kendi ilk argüman olarak gönderiyo 
kullanici_2 = Kullanici("Ayşe", 30)
kullanici_1.kullanici_bilgisi()         # Çıktı: Kullanıcı: Ahmet, 25

try:
    hatali_nesne = Kullanici("Ahmet")
except TypeError as hata_mesaji:
    print(f"Hata: {hata_mesaji}")
# Çıktı: Hata: Kullanici.__init__() missing 1 required positional argument: 'yas'