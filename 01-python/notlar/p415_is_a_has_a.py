# INHERITANCE -> Yanlış uygulama: her yeteneği miras almaya çalışmak 
class Logger:
    def log(self, mesaj):
        return f"[LOG] {mesaj}" 

class Veritabani(Logger):
    def kaydet(self, veri):
        print(self.log(f"Kalıtım ile: {veri} kaydedildi."))

# Veritabani bir Logger değildir halbuki... Onu yapabilir ama tümüyle o değildir.

yanlis_database = Veritabani()
yanlis_database.kaydet("Kullanici verisi")   
# Çıktı: [LOG] Kalıtım ile: Kullanici verisi kaydedildi.


# COMPOSITION -> Doğru Mimari: Bağımlılığı içeri almak (Has-A İlişkisi)
class DosyaLogger:
    def log(self, mesaj):
        return f"[DOSYA LOG] {mesaj}" 

class AgLogger:
    def log(self, mesaj):
        return f"[AĞ LOG] {mesaj}" 
# Birden fazla ata sınıf var kalıtım uygulamak için ...
# Farklı senaryolarda runtime esnasında "parent" değiştiremeyiz de!
# Dinamik olarak değiştirebilmek için -> Kompozisyon
# Çalışma zamanına istediğimiz logger'ı takıp çıkarabiliriz.

class DogruVeritabani:  

    # Veritabanı bir logger'a sahiptir deriz initialize ederken (Has-A)
    def __init__(self, logger_bileseni):
        self.logger = logger_bileseni   # Dinamik Enjeksiyon (Dependency Injection)

    def kaydet(self, veri):
        # İşlemi içteki nesneye devrediyoruz (delegation)
        print(self.logger.log(f"Kompozisyon ile: {veri} kaydedildi."))

dosya_database = DogruVeritabani(DosyaLogger()) 
ag_database = DogruVeritabani(AgLogger())

dosya_database.kaydet("Sipariş verisi")
# Çıktı: [DOSYA LOG] Kompozisyon ile: Sipariş verisi kaydedildi.
ag_database.kaydet("Sipariş verisi")
# Çıktı: [AĞ LOG] Kompozisyon ile: Sipariş verisi kaydedildi.


# Pratik Kısmı -> Oyun Karakteri Modelleme
"""
1. Kilic adında bir sınıf oluştur. İçinde saldir() metodu olsun ve "Kılıçla 50 hasar verildi!" döndürsün.
2. Kalkan adında bir sınıf oluştur. İçinde savun() metodu olsun ve "Kalkanla bloklandı!" döndürsün.
3. Savasci adında bir sınıf oluştur. __init__ metodu parametre olarak bir silah ve bir zirh nesnesi alsın (Kompozisyon).
4. Savasci sınıfında aksiyon_yap() adında bir metod yaz. Bu metod, içindeki silahın saldırısını ve zırhın savunmasını çağırıp
sonuçları ekrana print ile alt alta yazdırsın.
"""

class Kilic: 
    def saldir(self, hasar):
        return f"Kılıçla {hasar} hasar verildi!"

class Kalkan:
    def savun(self, basari: bool = True):
        if basari:
            return f"Kalkanla bloklandi."
        else: 
            return f"Koltuklanmis Kargi vuruşu yedin. gg!"
    
class Savasci:

    def __init__(self, silah, zirh):
        self.silah = silah
        self.zirh = zirh

    def aksiyon_yap(self, silah_hasar=50, savunma_basari=True):
        print(self.silah.saldir(silah_hasar))
        print(self.zirh.savun(savunma_basari))

benim_kilicim = Kilic()
benim_kalkanim = Kalkan()
karakter1 = Savasci(benim_kilicim, benim_kalkanim)
karakter1.aksiyon_yap(50, True)