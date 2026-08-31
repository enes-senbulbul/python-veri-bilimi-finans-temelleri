# Sozluk Olusturma
cihaz_durumu = {
    "sensor_id":"SN_901",
    "aktif": True,
    "sicaklik_gecmisi": [22.4, 23.1, 22.9]
}

# Deger Okuma, Değiştirme ve Yeni Ekleme
cihaz_durumu["aktif"] = False               # Var olan bir değeri güncelleme
cihaz_durumu["lokasyon"] = "Bina-A"         # Olmayan anahtara atama yapınca yeni kayıt ekler
cihaz_durumu.update({"lokasyon":"FEB", "versiyon":2})   # Toplu Güncelleme
cihaz_durumu.setdefault("versiyon", 99)     # O anahtar yoksa günceller, varsa değerine dokunmaz.
print(cihaz_durumu["versiyon"])

# Görünüm (View) Metotları
print(cihaz_durumu.keys())
print(cihaz_durumu.values())
print(cihaz_durumu.items())

# Güvenli erişim metodu .get()
ayarlar = {"timeout":30, "retry":3}

try:                                        # Doğrudan Erişim
    print(ayarlar["host"])
except KeyError as hata_mesaji:
    print(f"Hata yakalandi: {hata_mesaji}")
print(ayarlar.get("host"))                  # None
print(ayarlar.get("host", "127.0.0.1"))     # Yoksa bizim belirlediğimiz varsayılan değeri kullanır.

# Sözlük Metotları 
cihaz_durumu_shallow_kopya = cihaz_durumu.copy() 
cihaz_durumu_shallow_kopya.popitem()        # Son eklenen anahtar değer çiftini çıkarır.
print(cihaz_durumu_shallow_kopya)           # version:2 atılmış

# Pratik
profil = {
    "kullanici": "admin",
    "yetki_seviyesi": 2
}
profil["son_giris"] = "2023-10-01"
eposta = profil.get("eposta", "eposta_yok@sistem.local")
print("Atanan eposta:", eposta)