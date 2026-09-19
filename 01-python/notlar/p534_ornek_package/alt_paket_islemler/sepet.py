# Relative Import: 
# Bir üstteki dizin'e çıkıp o dizindeki ürünler modülüne erişiyoruz.
from ..urunler import urun_sorgula

def sepete_ekle(urun_id, adet):
    urun = urun_sorgula(urun_id)
    print(f"{adet} adet {urun["ad"]} sepete ekleniyor...")
    toplam_tutar = urun["fiyat"] * adet
    return toplam_tutar