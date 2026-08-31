# Tuple oluştururken parantez kullanmak yaygındır ama zorunlu değildir.
random_koordinat = (41.107062, 29.022986)
renk_kodu = 255, 128, 0     # Bu da bir tuple'dır.

# Tuple unpacking 
enlem, boylam = random_koordinat
print(f"Enlem: {enlem}, Boylam: {boylam}")

# Tek elemanlı tuple 
sahte_tuple = (5)
gercek_tuple = (5, )
print(type(sahte_tuple))
print(type(gercek_tuple))

# Tuple Metotları - Listedeki index ve count var sadece
meyveler = "elma", "elma", "armut", "muz", "elma"
print(meyveler.index("elma"))       # Değerin ilk indexini bulur
print(meyveler.count("elma"))       # Değerin kaç defa geçtiğini bulur

# Tuple - Swapping
a, b = 0, 100
a, b = b, a
print(a, b) 

# Immutability
ornek_tuple = (10, 20)
try:
    ornek_tuple[0] = 99
except TypeError as error_message:
    print(f"Hata yakalandi: {error_message}")

# Pratik
nokta = 15.5, -3.2, 8.9
x, y, z = nokta
print("Z ekseni degeri: ", z)