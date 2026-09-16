# Hataların hepsi aslında bir sınıftır. PascalCase ile yazılmış zaten.
# Programımıza özgü kendi hata türlerimizi de sınıf oluşturarak tanımlayabiliyoruz.

# En basit şekilde custom hata tanımlamak 
class StokYetersizHatasi(Exception):        # 'Exception' sınıfından kalıtım alınır.
    pass                                    # Sadece ismen tanımlanması bile yeterli.

# Gelişmiş/edge-case: Veri taşıyan custom hata tanımlamak
class BakiyeYetersizHatasi(Exception):
    def __init__(self, mevcut, istenen):
        self.mevcut = mevcut
        self.istenen = istenen
        self.fark = istenen - mevcut
        mesaj = f"İşlem reddedildi. {self.fark} TL eksik. (Mevcut: {self.mevcut}, İstenen: {self.istenen})"
        super().__init__(mesaj)         # super() ile parent sınıfın mesaj mekanizmasını tetikliyoruz.


def para_cek(bakiye, miktar):
    if miktar > bakiye:
        # Hata nesnesini oluşturup (instantiate) 'raise' anahtar kelimesiyle fırlatıyoruz
        raise BakiyeYetersizHatasi(bakiye, miktar)
    return bakiye - miktar


try: 
    yeni_bakiye = para_cek(1000, 1500)
except StokYetersizHatasi:              
    print("Stok problemi yaşandı")
except BakiyeYetersizHatasi as hata:
    print(f"Hata yakalandı: {hata}")
    print(f"Debug: Müşteri {hata.fark} TL açığa düştü.")

# Hata yakalandı: İşlem reddedildi. 500 TL eksik. (Mevcut: 1000, İstenen: 1500)
# Debug: Müşteri 500 TL açığa düştü.