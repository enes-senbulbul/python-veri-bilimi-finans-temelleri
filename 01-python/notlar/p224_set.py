# Küme Oluşturma ve Tekilleştirme (Duplicate Temizliği)
okumalar = [22, 25, 22, 23, 25, 25]
unique_okumalar = set(okumalar)
print(unique_okumalar)          # Kümelerde Sıra Yoktur, Rastgele Yazdırır

# Küme Oluşturma Tuzağı
sahte_bos_kume = {}
gercek_bos_kume = set()
print(type(sahte_bos_kume))
print(type(gercek_bos_kume))

# Küme Metotları - Ekleme/Çıkarma
etiketler_a = {"python", "veri-bilimi", "api"}
etiketler_b = {"python", "sql", "finans"}
etiketler_a.add("finans")           # Bir eleman ekler
etiketler_b.remove("finans")        # Bir eleman çıkarır - Hata verebilir.
etiketler_b.discard("finans")       # Bir eleman çıkartır - Zaten yoksa hata vermez.
etiketler_b.update(["ml","quantative-analysis"])    # Bir iterable ekler
print(etiketler_a, etiketler_b)

# Küme Metotları - Cebirsel Operasyonlar / In-place değil, küme döndürür
print(etiketler_a.intersection(etiketler_b))
print(etiketler_a.union(etiketler_b))
print(etiketler_a.difference(etiketler_b))
print(etiketler_b.difference(etiketler_a))
print(etiketler_a.symmetric_difference(etiketler_b))

# Küme Metotları - Kapsama ve Alt kümesi olma
kume_a = {"A","B","C","D"} 
kume_b = {"A","B","C"}
kume_c = {"X","Y","Z"}
print(kume_b.issubset(kume_a))
print(kume_a.issuperset(kume_b))
print(kume_c.isdisjoint(kume_a))    # Hiç ortak elemanları yok mu -> True