import os
import sys;
print("\n".join(sys.path))

# Çıktı: 
# c:\Users\enes\...\python-veri-bilimi-finans-temelleri\01-python\notlar    -Güncel Dizin-
# C:\Users\enes\...\Python313\python313.zip
# C:\Users\enes\...\Python\Python313\DLLs                                   -C dilinde derlenmiş modüller-
# C:\Users\enes\...\Python\Python313\Lib                                    -Standart kütüphane-
# C:\Users\enes\...\Python\Python313            
# C:\Users\enes\...\Python\Python313\Lib\site-packages                      -pip paketleri-

try:
    import gizli_modul                                              # type: ignore
except ModuleNotFoundError as hata:
    print(f"Hata: {hata}")
    # Yani haliyle öyle bir lokasyona bakmadığından bulamaz.

mutlak_lokasyonu = os.path.abspath("notlar/p535_syspath_circular_imp/")
sys.path.append(mutlak_lokasyonu)

import modul_iceren_dosya.gizli_modul as modul                      # pyright: ignore[reportMissingImports] -> Kod çalışmasına rağmen bu hata bir türlü susmadı.
modul.reveal_the_secret()     
# Çıktı: Modül artık Python tarafından görülüyor. sys.path'e eklemek işe yaradı. 


# --- Circular Import ---
try:
    from paket_circular_import.musteri import alisveris_yap         # pyright: ignore[reportMissingImports]
    sonuc = alisveris_yap("Ahmet", "Mekanik Klavye")
    print(sonuc)
    
except ImportError as hata:
    print(f"Kritik Mimari Hatası: {hata}")

# Çıktı: 
# [Ahmet] alışveriş sepetini onaylıyor...
# Fatura Kesildi: Kayıtlı Müşteri (Ahmet) | Satın Alınan: Mekanik Klavye