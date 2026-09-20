# Üç tane önemli Python standart library modülünü bu dosyada çalışacağız bakalım
# 1 - math  ->  bilimsel fonksiyonlar ve sabitler
# 2 - os    ->  dosya, klasör(dizin) işlemleri 
# 3 - sys   ->  CLI ile iletişim

# --- MATH ---     
# Veri Bilimci olacağım senaryoda bunları teker teker deneyip tanışmam lazım
# Yoksa ben de ameleliği pek sevmiyorum yani kim bunları teker teker denemekle - bi de formatlı şekilde yazdırmakla- uğraşacak 
# Bi de leetcode için bi Python'da ne var ne yok görmem de lazım
import math     

print("\n--- 1. 'math' sabitleri ---".upper())
print(f"pi sabiti:    {math.pi:.5f}")
print(f"euler sabiti: {math.e:.5f}")
print(f"tau sabiti:   {math.tau:.5f}")
print(f"sonsuzluk     {math.inf}")
print(f"Not a number: {math.nan}")

print("\n--- 2. 'math' Yuvarlama fonksiyonları ---".upper())
print("Built-in 'round' fonksiyonumuzla yuvarlama:", round(math.e))
print("Tavana (ceil) yuvarlama:", math.ceil(math.e))
print("Tabana (floor) yuvarlama:", math.floor(math.pi))
print("Ondalık kısmı atma (trunc):", math.trunc(-9.9999))

print("\n--- 3. 'math' mutlak değer ve üs alma ---".upper())
print("Mutlak değer alma (abs -> built-in'dir. Aldığı parametrenin tipini döndürür):", type(abs(-99)))
print("Mutlak değer alma (math.fabs -> math ile geliyor, her zaman 'float' döndürür):", type(math.fabs(-99)))
print("Üs alma, built-in '**' ve pow'dan farkı her zaman 'float' döndürmesi (MATLAB mantığı)", math.pow(2, 3))
print("Karekökünü alma:", math.sqrt(16))
print("Faktöriyelini alma:", math.factorial(5))
print("EBOB - Greatest Common Factor - GCD:", math.gcd(8, 12))
print("EKOK - Lowest Common Multiple - LCM:", math.lcm(8, 12))

print("\n--- 4. 'math' Kombinasyon ve Permütasyon ---".upper())
print("Kombinasyon:", math.comb(6,3))
print("Permütasyon:", math.perm(6,3))

print("\n--- 5. 'math' üstel ve logaritmik fonksiyonlar ---".upper())
print("Farklı tabanlarda log(2 parametreli):", math.log(243, 3))
print("Doğal logaritma (1 parametreli) :", math.log(pow(math.e, 3)))
print("2 tabanında log2:", math.log2(1024))
print("10 tabanında log10:", math.log10(1_000_000))
print("Doğal Üstel Fonksiyon (e^x):", math.exp(1))
print("2 tabanında Üstel Fonksiyon (2^x):", math.exp2(7))

print("\n--- 6. 'math' Trigonometrik Fonksiyonlar (Her Zaman Radyan) ve Derece Dönüşümleri ---".upper())
print("Sinüs, Sine:", math.sin(math.pi / 2))
print("Kosinüs, Cosine:", math.cos(math.pi))
print("Tanjant, Tangent:", math.tan(math.pi / 4))  
print("arcsin:", math.asin(-1))
print("arccos:", math.acos(-1))
print("arctan:", math.atan(math.inf))    # Cidden pi/2 çıkıyor sonuç
print("arctan2 (koordinat):", math.atan2(1,1))   # pi/4
print("Açı dönüşümü radyan -> derece:", math.degrees(math.pi))  # 180.0
print("Açı dönüşümü derece -> radyan:", math.radians(180))      # 3.14159...


print("\n--- 7. 'math' Predicator Fonksiyonlar (isX() -> bool döndüren) ---".upper())
print("Aralarındaki fark relative tolerans değerinden az mı", math.isclose(0.1+0.2, 0.3))
# Default değer relative tolerans rel_tol=1e-09     -> Aralarındaki fark bundan küçük olmalı
# Default değer absolute tolerans abs_tol=0.0       -> Aralarındaki fark bundan büyük olmalı
print("Sonsuz mu?:", math.isinf(float("inf")))
print("NaN mı?:", math.isnan( math.inf / math.inf ))    # Belirsizlikler de NaN
print("Sonlu mu?", math.isfinite(3))


print("\n--- 8. 'math' Kümülatif Fonksiyonlar (sum, prod) ---".upper())
sayilar = range(1,6)
print("1'den 5'e kadar sayıların toplamı (built-in sum'dan farkı float döndürmesi):", math.fsum(sayilar))
print("1'den 5'e kadar sayıların çarpımı:", math.prod(sayilar))


print("\n--- 9. 'math' Özel Fonksiyonlar  ---".upper())
a = (2, 3, 5)
b = (1, 4, 8)
print("Öklidyen mesafe:", math.dist(a, b))
print("Hipotenüs:", math.hypot(9,40))
print("Gamma Fonksiyonu: ", math.gamma(6))
print("Gauss Hata Fonksiyonu: ", math.erf(0.5)) 