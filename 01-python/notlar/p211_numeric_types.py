# Arithmetic Tipler 
tam_sayi = 42
ondalikli_sayi = 3.14159
karmasik_sayi = 2 + 3j

# f-string 
print(f"42'nin tipi: {type(tam_sayi)}")
print(f"pi sayisinin ilk 3 ondaligi: {ondalikli_sayi:.3f}")

# Aritmetik Operatörler
a = 15
b = 4

toplam = a + b
fark = a - b
carpim = a * b 
gercek_bolme = a / b    # Her zaman float döndürür.
tam_bolme = a // b      # Her zaman integer döndürür.
kalan = a % b
us_alma = a ** b

# Complex Sayı Özellikleri ve Metotları 
z = 2 + 3j
print(z.real)
print(z.imag)
print(z.conjugate())

# Sayısal Tiplerle Çalışan Diğer Built-in Fonksiyonlar
number_a = 17.6823
print(round(number_a))
print(round(number_a, 1))
print(round(number_a, 2))

# Pratik 
fiyat = 299.99
adet = 3
kdv_orani = 0.18

ara_toplam = fiyat * adet
kdvli_toplam = ara_toplam * (1 + kdv_orani)

odenecek_tutar = int(kdvli_toplam)
print(f"Odenecek tam tutar: {odenecek_tutar} TL") 