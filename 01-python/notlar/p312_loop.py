# for loop -> Iteration sayısı belli
carpimlar_toplami = 1
for i in range(1, 6):
    carpimlar_toplami *= i
print("5 faktoriyel = {}".format(carpimlar_toplami)) 

# while loop -> Koşul sağlandıkça döngü devam eder
hata_payi = 10.0
while hata_payi > 1.0:
    hata_payi /= 2
    print(f"Güncel hata: {hata_payi}")

# for döngüsü ile iterable'lar üzerinde gezinme - break ve continue
okumalar = [22, 24, 12, 26, 30, 19, 999, 23, 25]
for sicaklik in okumalar:
    if sicaklik == 999:
        print("Sensör hatası, döngü kırılıyor.")
        break
    if sicaklik > 20:
        continue
    print(f"Soğuk gün! Sicaklik: {sicaklik} C")