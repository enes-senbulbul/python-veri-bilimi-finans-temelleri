# Fonksiyon Tanımı
def kinetik_enerji(kutle, hiz):             # Dönüş tipi ve adeti belirtmiyoruz
    enerji = 0.5 * kutle * (hiz**2)
    return enerji

sonuc = kinetik_enerji(10, 5)               # Positioned Arguments
sonuc_2 = kinetik_enerji(hiz=5, kutle=10)   # Keyword Arguments
print(f"Enerji: {sonuc} Joule")
print(f"Enerji: {sonuc_2} Joule")


# Default Parametreli Fonksiyon Tanımı
def logaritma_al(deger, taban=10):
    import math
    return math.log(deger, taban)

print(logaritma_al(100))
print(logaritma_al(100,100))


# Hafızada Kalan Liste Tuzağı 
def hatali_kayit(veri, log_listesi=[]):
    log_listesi.append(veri)
    return log_listesi

print(hatali_kayit("elma"))
print(hatali_kayit("armut"))     # Önceki fonksiyondan kalan "elma" da var. 
# Boş liste bir kere oluşturuluyor o da fonksiyon tanımlanırken

# Doğru Kullanım - None ve Truthiness Kontrolü
def guvenli_kayit(veri, log_listesi=None):
    if log_listesi is None:      # "==" yerine "is". Tüm None'lar aynı nesnedir.
        log_listesi = []
    log_listesi.append(veri)
    return log_listesi

print(guvenli_kayit("elma"))
print(guvenli_kayit("armut")) 


# Pratik
def sicaklik_donustur(derece, birim="C"):
    if birim == "C":
        return (derece*1.8)+32
    elif birim == "F":
        return (derece-32)/1.8

test1 = sicaklik_donustur(100)
print(f"100 C = {test1} F")
test2 = sicaklik_donustur(212, "F")
print(f"212 F = {test2} C")