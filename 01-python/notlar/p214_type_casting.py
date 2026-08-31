# Tip Dönüşümleri   str -> float, float -> int
ham_veri = "42.8"
ondalikli_deger = float(ham_veri)
tamsayi_deger = int(ondalikli_deger)
print(tamsayi_deger)    # Yuvarlama yapmaz. Ondalık kısmi keser.

# Tip Sorgulama 
print(type(5))              # Çıktı: <class 'int'>
print(isinstance(5, int))   # Çıktı: True
print(isinstance(5, (int, float, complex))) # Birden fazla tip aynı anda sorgulanabiliyor.

# Dinamik typing 
"""
C veya Java'da değişken, tipi önceden belirlenmiş bir "kutu"dur ve içine sadece
o tipten veri konabilir. Python'da ise değişkenler (örneğin x ), hafızada nerede
durduğu belli olan nesnelere (objelere) yapıştırılmış basit birer "etiket"ten
ibarettir. Etiketi bir tamsayıdan söküp bir metne yapıştırabilirsin.
"""

etiket = 10
print(type(etiket))

etiket = "Değisim"      # Aynı etiket başka nesneyi gösterir.
print(type(etiket))

# Strong typing örneği
"""
Güçlü (Strong) Tipleme İhlali Birçok dilde 5 + "5" işlemi örtük olarak "55" (string)
dönebilir. Python buna izin vermez, matematiksel güvenliği ön planda tutar
ve açık (explicit) bir dönüşüm ister. Hatayı bizzat görelim:
"""
metin_sayi = "5"
gercek_sayi = 5
try:
    hatali_sonuc = metin_sayi + gercek_sayi
except TypeError as error_message:
    print(f"Hata yakalandi: {error_message}")
# JavaScript olsaydı (weakly typed bir dil) kendiliğinden bu dönüşümü yapar ve 
# 55 sonucunu verirdi. (implicit type conversion)
print(int(metin_sayi) + gercek_sayi) # Explicit type conversion


# Pratik
gelen_sicaklik = "  -12.9 C  "
temiz_metin = gelen_sicaklik.strip().replace("C","").strip()
ondalikli_sicaklik = float(temiz_metin)
tamsayi_sicaklik = int(ondalikli_sicaklik)
print(tamsayi_sicaklik)