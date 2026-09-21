from datetime import datetime, date, timedelta, timezone


su_an = datetime.now()                      # Yerel saati saklamak
spesifik_an = datetime(2026, 9, 21, 5, 2)   # 21.09.2026 05.02
print("UTC+3 - İstanbul:")
print(f"Yıl: {su_an.year} | Ay: {su_an.month} | Gün: {su_an.day} | Saat: {su_an.hour}")

su_an_utc = datetime.now(timezone.utc)      # Daha güvenli olarak "UTC" saati saklamak
print("UTC - Coordinated Univ. Time:")
print(f"Yıl: {su_an_utc.year} | Ay: {su_an_utc.month} | Gün: {su_an_utc.day} | Saat: {su_an_utc.hour}")

# strftime - String format time - Zaman nesnesini formatlı string'e dönüştürmemize yarıyor.
zaman_metni = spesifik_an.strftime("%d/%m/%Y %H:%M")
print(zaman_metni)

# strptime - String parse time - Dışarıdan (API, CSV vs.) gelen str tarihi time nesnesine çevirme
zaman_bilgisi = "31-12-2026"
zaman_nesnesi = datetime.strptime(zaman_bilgisi, "%d-%m-%Y")
zaman_metni_2 = zaman_nesnesi.strftime("%d/%m/%Y")
print(f"Api'dan çekilen zaman: {zaman_metni_2}")

# timedelta - Zaman Aritmetiği 
gelecek_tarih = su_an + timedelta(days=5, hours=12)
print(type(gelecek_tarih - su_an))      # .ıktı: <class 'datetime.timedelta'> (timedelta Nesnesi)

# Epoch Zamanına/dan (timestamp) Çeviri
# ÖNEMLİ: Zamanı veritabanlarında, log dosyalarında vs. her zaman ya UTC zaman diliminde ya da epoch zamanı olarak saklamalıyız. 
epoch_su_an = su_an.timestamp()
epoch_ilk_gun = datetime(1970, 1, 2, 0, 0, tzinfo=timezone.utc).timestamp() 
print(epoch_ilk_gun)    # Çıktı: 86400.0 -> Bir günün bu kadar saniye ediyor :3
normal_su_an = datetime.fromtimestamp(epoch_su_an)

# Kod Uygulama
def abonelik_durumu(bitis_tarihi_str):
    bitis = datetime.strptime(bitis_tarihi_str, "%d-%m-%Y")
    fark = bitis.date() - datetime.now().date()     # Yalnızca tarihleri karşılaştırmak için 'date' metodu
    if fark.days < 0:
        return f"Süre {abs(fark.days)} gün önce doldu."
    return f"Sürenin bitmesine {fark.days} gün kaldı."

print(abonelik_durumu("12-10-2026"))