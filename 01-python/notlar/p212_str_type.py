# String tanımlama ve formatted string
isim = "Ahmet"
dil = "Python"
karsilama = f"Merhaba {isim}, {dil} öğreniyorsun."
print(karsilama)

# String metotları ve metot chaining
kirli_veri = "    vERi biLimİ     "
temiz_veri = kirli_veri.strip().lower().title()
print(f"Orijinal: '{kirli_veri}' -> Temiz: '{temiz_veri}'")

# Parçalama ve değiştirme
dosya_adi = "finans_raporu_2024.csv"
yeni_dosya = dosya_adi.replace(".csv", ".xlsx")
parcalar = yeni_dosya.split("_")
print(yeni_dosya)
print(parcalar)

# Pratik
eposta = "  kullanici@Sirket.COM   "
standart_eposta = eposta.strip().lower()
print(f"Kaydedilecek e-posta: {standart_eposta}")