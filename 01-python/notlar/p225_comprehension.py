# List Comprehension
sicakliklar_c = [22.5, 25.0, 30.2, 18.7, 27.1]
sicakliklar_f = [sicaklik*9/5+32 for sicaklik in sicakliklar_c]
print(sicakliklar_f)

# Koşullu List Comprehension
sicak_gunler_sicaklik = [sicaklik for sicaklik in sicakliklar_c if sicaklik >= 25]
print(sicak_gunler_sicaklik)
sicak_gunler_index = [sicakliklar_c.index(sicaklik) for sicaklik in sicakliklar_c if sicaklik >= 25]
print(sicakliklar_c)
print(sicak_gunler_index)

# Dict Comprehension
urun_fiyatlari = {"elma":12, "armut":18, "muz":9}
kdv = 1.20
kdv_dahil = {urun: round(fiyat*kdv,2) for (urun, fiyat) in urun_fiyatlari.items()}
print(kdv_dahil)

# Set Comprehension
kelimeler = ["elma","elma","armut","kivi","armut"]
benzersiz_uzunluklar = {len(k) for k in kelimeler}
print(benzersiz_uzunluklar)

# Nested Comprehension
matris = [[1,2],[3,4],[5,6]]
duzlestirilmiş = [sayi for satir in matris for sayi in satir]
print(duzlestirilmiş)