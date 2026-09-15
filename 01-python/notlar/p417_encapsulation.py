# "We are all consenting adults here" -> Gerçek anlamda private değişken olayı yok Python'da

class Urun:
    def __init__(self, ad, fiyat):
        self.ad = ad
        # tek alt çizgi ile "protected" olduğunu işaret ediyoruz. Sadece işaret ediyoruz xd
        # "Bu değişken doğrudan ellenmemelidir."
        self._fiyat = None
         # __init__ içinde de setter mantığını kullanmak için property üzerinden atama yapıyoruz. 
        self.fiyat = fiyat     

    @property       # Okuyucu (Getter): Dışarıdan 'urun.fiyat' yazıldığında bu metot çalışır.
    def fiyat(self):
        return self._fiyat 

    @fiyat.setter   # Yazıcı (Setter): Dışarıdan 'urun.fiyat=50' yazıldığında bu metot çalışır.
    def fiyat(self, yeni_deger):
        if yeni_deger < 0:
            raise ValueError("Fiyat negatif olamaz!")
        self._fiyat = yeni_deger


bilgisayar = Urun("Laptop", 25000)

# Okuma İşlemi -> Dışarıdan normal gözüküyor ama bunu sağlayan sınıfın içindeki property
print(bilgisayar.fiyat)     # Çıktı: 25000

# Yazma İşlemi -> Aynı şekilde dışarıdan normal gözüküyor ama tüm olay içeride
bilgisayar.fiyat = 24000
print(bilgisayar.fiyat)     # Çıktı: 24000

try:
    bilgisayar.fiyat = -10000
except ValueError as hata_mesaji:
    print(f"Hata Yakalandı: {hata_mesaji}")


# Ekleme: Aslında çift alt çizgi ile "private-like" da yapabiliyoruz. "proctected"dan farklı olarak
# python Name Mangling yaptığından dolayı kalıtımda çocuk sınıflar ilgili değişkeni değiştiremiyor. 
class Sunucu:               # Parent Class
    def __init__(self):
        self.__durum = "Aktif"      # Arka planda: self._Sunucu__durum

    def calistir(self):
        return f"Sunucu durumu: {self.__durum}"

class OzelSunucu(Sunucu):   # Derived Class 
    def __init__(self):
        super().__init__()
        self.__durum = "Bakımda"    # Bu satır artık parent class'ın __durum değişkenine dokunmaz.
        # Python bunu da self._OzelSunucu__durum olarak saklayacak. Tamamen farklı, izole bir isim
        # Bu, büyük projelerde gerçek hayatta olan bir hatadır: Alt sınıf yazan geliştirici, parent
        # sınıfın iç değişken isimlerini bilmek zorunda değildir ama yine de kazara üzerine yazabilir.
 
ozel_sunucu1 = OzelSunucu()
print(ozel_sunucu1.calistir())      
# Çıktı: Sunucu durumu: Aktif
print(ozel_sunucu1.__dict__)        
# Çıktı: {'_Sunucu__durum': 'Aktif', '_OzelSunucu__durum': 'Bakımda'}
# İki ayrı, birbiriyle çakışmayan değişken oluştu :)