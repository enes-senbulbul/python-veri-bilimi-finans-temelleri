import json
import csv 

# Düz Metin (Text) Formatı 
with open("notlar/p521_metin.txt", "w", encoding="utf-8") as dosya:    # w ile yazma
    dosya.write("İlk satır\nİkinci satır")

with open("notlar/p521_metin.txt", "r", encoding="utf-8") as dosya:    # r ile okuma
    icerik = dosya.read()
    print("--- Metin Dosyası ---")
    print(icerik)


# JSON Formatı -> Sözlükler ve API verilerini kaydetmek için 
kullanici = {
    "id": 10001,
    "isim": "Mehmet", 
    "aktiflik": True,
    "yetkiler": ["admin"]
}

with open("notlar/p521_api_veri.json", "w", encoding="utf-8") as dosya:
    json.dump(kullanici, dosya)     
    # dump() -> python sözlüğünü JSON dosyasına yazar

with open("notlar/p521_api_veri.json", "r", encoding="utf-8") as dosya:
    gelen_veri = json.load(dosya)
    # load() -> JSON dosyasını okuyup python sözlüğüne çevirir.
    print("--- JSON Dosyası ---")
    print(f"Kullanıcı: {gelen_veri.get("isim")}\nAktif mi? {gelen_veri.get("aktiflik")}")



# CSV Formatı -> Excel benzeri tablo verilerini kaydetmek için
tablo = [
    ["Ürün", "Fiyat"],
    ["Klavye", 1500],
    ["Mouse", 500]
]

with open("notlar/p521_tablo_veri.csv", "w", newline="", encoding="utf-8") as dosya:
# newline="" parametresi CSV yazarken Windows'ta oluşan ekstra boş satırları engelliyormuş.
    yazici = csv.writer(dosya)
    yazici.writerows(tablo)         # Birden fazla satırı tek seferde yazar.

with open("notlar/p521_tablo_veri.csv", "r", encoding="utf-8") as dosya:
    okuyucu = csv.reader(dosya)
    print("--- CSV Dosyası ---")
    for satir in okuyucu:
        print(" | ".join(satir))