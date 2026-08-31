# Liste oluşturma  
sensor_verileri = [24.5, 25.1, "HATA", 23.8, 24.8]  # Farklı tipte veri içerebilir.

# Indeksleme (list -> Sequence)
print(sensor_verileri[0])
print(sensor_verileri[-1])

# Değiştirme (list -> Mutable)
sensor_verileri[2] = 24.9
print(sensor_verileri)

# Dilimleme/Slicing 
print(sensor_verileri[1:4])     # 1 dahil ama 4 dahil değil
print(sensor_verileri[::-1])    # listeyi tersine çevirir.

# Sınır aşımı
meyveler = ["elma", "armut"]
try:
    print(meyveler[5])
except IndexError as error_message:
    print(f"Index hatasi: {error_message}")

print(meyveler[5:10])   # Indexlemenin aksine slicing sınır aşımında çökmez. Boş liste döndürür.


# Liste Metotları - Ekleme/Çıkarma
sensor_data = [24.5, 25.1, "HATA", 23.8, 24.0]
sensor_data.append(26.3)        # Ekleme - sona
sensor_data.insert(0, 22.0)     # Ekleme - belirtilen index
print(sensor_data.pop())        # Çıkarma - sondan / Değer döndürür
print(sensor_data.pop(2))       # Çıkarma - belirtilen index 
sensor_data.remove(24.0)        # Çıkarma - belirtilen eleman, ilk eşleşen
sensor_data.clear()             # Listenin içindekileri temizler
del sensor_data                 # Listenin kendisini siler.

# Liste Metotları - Sıralama
alfabe = ["a", "c", "f", "g", "e", "b", "d"]
alfabe.reverse()                # Sıradan bağımsız ters çevirir.
print(alfabe)
alfabe.sort(reverse=True)       # Sıralama - Artan sıra
print(alfabe)
alfabe.sort()
print(alfabe)                   # Sıralama - Azalan sıra

# Liste Kopyalama
alfabe2 = alfabe.copy()         # Doğru kopyalama - Aynı içerik ile yeni nesne
alfabe3 = alfabe[:]
alfabe4 = list(alfabe)          
alfabe5 = alfabe                # Yanlış kopyalama - Aynı liste nesnesini gösterir.

# Liste Eleman Arama
meyveler = ["elma", "elma", "armut", "muz", "elma"]
print(meyveler.index("elma"))       # Değerin ilk indexini bulur
print(meyveler.count("elma"))       # Değerin kaç defa geçtiğini bulur


# Pratik
olcumler = [10, 12, 15, 14, 18, 20, 22]
son_uclu = olcumler[-3:]
olcumler.append(25)
print("Son 3 eleman:", son_uclu)
print("Guncellenmis liste:", olcumler)