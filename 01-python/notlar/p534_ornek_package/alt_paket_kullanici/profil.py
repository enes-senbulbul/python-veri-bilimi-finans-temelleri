# Bir üste çıkıp diğer alt pakete gir ve oradaki sepet.py modülüne eriş
from ..alt_paket_islemler.sepet import sepete_ekle
from ..urunler import stok_kontrol, stok_dus, urun_sorgula

class Kullanici:

    def __init__(self, isim, bakiye):
        self.isim = isim
        self.bakiye = bakiye
        self.aldiklari = []
        self.islem = 1

    def alisveris_yap(self, urun_id, adet):

        print(f"İşlem #{self.islem}")

        try:
            stok_kontrol(urun_id, adet)
            tutar = sepete_ekle(urun_id, adet)

            if self.bakiye < tutar:
                raise ValueError(f"Bakiye yetersiz. Gereken: {tutar}, Tutar: {self.bakiye}")

            # Alım başarılı
            bakiye_once = self.bakiye
            self.bakiye -= tutar
            alinan_urun = urun_sorgula(urun_id)["ad"]
            self.aldiklari.append(f"{adet} x {alinan_urun}")

            print(f"Onaylandı. Ödemeniz alındı. Bakiye({self.isim}): {bakiye_once} -> {self.bakiye}")
            stok_dus(urun_id, adet)
            return True
        
        except ValueError as hata:
            print(f"{self.isim} <- İşlem Başarısız: {hata}")
            return False
        
        finally:
            self.islem += 1
            print("")