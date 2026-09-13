# Parametreli decoratorler, üst üste decorator kullanımı, late binding vs. hepsini p399'da detaylı çalıştım.

# Decorators -> Closure mekanizması üzerine kuruludur.
# Dış fonksiyon iç fonksiyonu içine hapseder, iç fonksiyon ise ekstra işlemleri 
# yapıp orijinal fonksiyonu döndürür.

import time
from functools import wraps     

def sure_olc(fonksiyon):
    @wraps(fonksiyon)       # wrapper'ın orijinal fonksiyonun metadatasını değiştirmesini engeller.
    def wrapper(*args, **kwargs):
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        gecen_sure = time.perf_counter() - baslangic
        print(f"[Log] Fonksiyonun çalışma süresi: {gecen_sure} sn")    # İç fonksiyonun ekstra davranışları
        return sonuc
    return wrapper


@sure_olc
def agir_hesaplama(limit):
    """Verilen limite kadar olan sayıların karelerini toplar"""
    return sum(x**2 for x in range(limit))

print("Sonuç:", agir_hesaplama(3000))
print("Metadatası korunur:", agir_hesaplama.__doc__, agir_hesaplama.__name__, sep="\n")