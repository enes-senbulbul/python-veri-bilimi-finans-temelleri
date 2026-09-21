import itertools as it      # it conventional alias'mış


# Kombinasyon 
harfler = ["A", "B", "C"]
kombinasyonlar = list(it.combinations(harfler, 2))  # Iteratorü evaluate etmek için list()
print(f"Kombinasyonlar: {kombinasyonlar}")

# Permütasyon
permutasyonlar = list(it.permutations(harfler, 2))
print(f"Permütasyonlar: {permutasyonlar}")

# Kartezyen Çarpım
sayilar = [1, 2, 3]
kartezyen = list(it.product(harfler, sayilar))
print(f"Kartezyen Çarpımlar: {kartezyen}")

# Sonsuz İteratorlerle Çalışırken Sınır Koymak (islice)
cift_iter = it.count(10,2)    # 10, 12, 14 ... sonsuza kadar evaluate eder sınır koyulmazsa
ilk_bes_cift = list(it.islice(cift_iter, 5))
print(f"Dilimlenmiş Sonsuz Dizi: {ilk_bes_cift}")

# Bellek dostu veri birleştirme (chain)
veri_akisi1 = [1, 2, 3]      # İki büyük boyutlu dosyayı doğrudan birleştirmek çok maliyetli
veri_akisi2 = [4, 5, 6]      
# Onun yerine bir iterator oluşturuyoruz. Sırayla ilkindeki elemanları, bitince de ikincisindeki elemanları işaret eder.
birlestirilmis_dosya_iter = it.chain(veri_akisi1, veri_akisi2)