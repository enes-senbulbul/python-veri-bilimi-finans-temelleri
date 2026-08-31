# Mantıksal değerler ve hiçlik nesnesi
sistem_aktif = True
hata_var = False
kullanici_id = None     # Veritabanından henüz çekilmemiş

# Mantıksal operatörler 
sisteme_giris = sistem_aktif and not hata_var
print(f"Giris yapilabilir mi? {sisteme_giris}")

# Dogruluk degeri analizi
print(f"0'in dogruluk degeri: {bool(0)}")
print(f"Bos string'in dogruluk degeri: {bool('')}")
print(f"None nesnesinin dogruluk degeri: {bool(None)}")
print(f"String'in dogruluk degeri: {bool('Python')}")
print(f"Negatif sayinin dogruluk degeri: {bool(-5)}")
y = float('nan') # Not a number
print(f"NaN dogruluk degeri: {bool(y)}")

# None nesnesi bellekte tek olduğu için == değil "is" ile kontrol edilmelidir. (Best-Practice) 
x = None
print(x == None)    # Çalışır ama best practise değildir.
print(x is None)

# Pythonic boşluk kontrolü
gelen_veri = []

if not gelen_veri:  # len() ile uzunluk ölçme!
    print("Veri bos")
else:
    print("Veri isleniyor.")
