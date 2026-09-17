from p532_script_main import *      # p532'nin içindeki nesneleri p533'ün namespace'ine boşaltır.

# Şu nesneler hariç
# 1) __all__ içinde ismi string olarak alınan fonksiyonlar/değişkenler
# 2) __all__ içine alınıp alınmaması fark etmeksizin "_" ile başlayan fonksiyonlar/değişkenler
# 3) ve tabiki de __main__ içinde olanlar

merhaba("Ali")       # p532.merhaba dememize gerek yok, merhaba direkt global namespace'te
hal_hatir_sor()
gorusuruz("Ali")

try:
    borc_iste(500)  # type: ignore[name-defined] 
except NameError as hata_mesaji:
    print("'borc_iste' p532'de __all__ içinde olmadığından namespace'e eklenmedi!")

try:
    _gizli_fonksiyon()  # type: ignore[name-defined]
except NameError as hata_mesaji:
    print("'_gizli_fonksiyon' namespace'e eklenmedi!")