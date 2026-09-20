import sys
import os
import importlib 

# SYS.PATH'ın modüllerimizi 01-python(CWD)/notlar içinde bulabilmesi için
mevcut_dizin = os.getcwd()
sys.path.insert(0, mevcut_dizin)
print(f"Mevdut working dir (CWD): {mevcut_dizin}")

aktif_eklentiler = [
    "notlar.p536_dinamik_paket.eklenti_pdf",
    "notlar.p536_dinamik_paket.eklenti_csv",
    "notlar.p536_dinamik_paket.bozuk_eklenti",
    "notlar.p536_dinamik_paket.olmayan_eklenti"
]

islenecek_veri = "2026_Veri_Seti"

for eklenti in aktif_eklentiler:
    print(f"'{eklenti}' yükleniyor...")
    try: 
        modul_nesnesi = importlib.import_module(eklenti)
        # 'modul_nesnesi' nesnenisin içinde "disari_aktar" fonksiyonu yoksa AttributeError ile çökmesini
        # engellemek için o attribute'un varsayılan bir değeri olması sağlanır. Burada 'None'. 
        islem_fonksiyonu = getattr(modul_nesnesi, "disari_aktar", None)
        if islem_fonksiyonu:    # modul_nesnesi'ndeki "disari_aktar" None değilse
            sonuc = islem_fonksiyonu(islenecek_veri)
            print(f"Veri başarıyla işlendi. Veri -> {sonuc}")
        else:
            print("[Hata] Eklenti yüklendi ancak eklenti içinde 'disari_aktar' isimli fonksiyon bulunamadı")
    except ModuleNotFoundError:
        print("[Hata] Modülün kendisi ortada yok bu sefer.")
    print("-"*30)



# Çıktı:
# 'notlar.p536_dinamik_paket.eklenti_pdf' yükleniyor...
# Veri başarıyla işlendi. Veri -> (PDF Eklentisi): 2026_Veri_Seti dışarı aktarıldı.
# ------------------------------
# 'notlar.p536_dinamik_paket.eklenti_csv' yükleniyor...
# Veri başarıyla işlendi. Veri -> (CSV Eklentisi): 2026_Veri_Seti dışarı aktarıldı.
# ------------------------------
# 'notlar.p536_dinamik_paket.bozuk_eklenti' yükleniyor...
# [Hata] Eklenti yüklendi ancak eklenti içinde 'disari_aktar' isimli fonksiyon bulunamadı
# ------------------------------
# 'notlar.p536_dinamik_paket.olmayan_eklenti' yükleniyor...
# [Hata] Modülün kendisi ortada yok bu sefer.
# ------------------------------