# Decorators aşırı zormuş. Bu sebeple Corey Schafer'la en baştan başlayacağım.
# 1) First-Higher Class Functions Farkı 
# 2) Closure 
# 3) Decorators 

# --- First-Higher Class Functions ---
# First class fonksiyonlar, diğer first-class nesnelerin hepsine yapabildiğimiz şeyleri ona da 
# yapabildiğimiz fonksiyonlardır. 
# Bu şeyler: 
# * Argüman olarak verilebilmek,
# * bir fonksiyon tarafından döndürülebilmek, 
# * bir değişkene atanabilmek
# Sadece veri tipleri (sayılar, metinler, nesneler vb.) üzerinde işlem yaparlar. Fonksiyon işlemezler. 

# ^^^ Bir fonksiyonu değişkene atayabilmek ne demek?
def square(x):
    return x*x

f = square(5)   # Bir fonksiyonun "döndürdüğü değeri atamak" kesinlikle değildir!!! 
print(square)   # Çıktı: <function square at 0x0000025F665DCEA0>
print(f)        # Çıktı: 25, burada f integerdır.

f = square      # Parantezler fonksiyonu "çalıştırır". Biz çalıştırmadan kendisini atıyoruz.
print(square)   # Çıktı: <function square at 0x0000025F665DCEA0>
print(f)        # Çıktı: <function square at 0x0000025F665DCEA0>
print(f(5))     # Çıktı: 25, burada f artık kendisi de bir fonksiyondur.

# ^^^ Bir fonksiyonu argüman olarak vermek + fonksiyon tarafından döndürülebilmesi ne demek?
# Higher-order function: Başka fonksiyonları argüman olarak alabilen veya sonuç olarak fonksiyon 
# döndürebilen fonksiyonlara denir. Örn: map() fonksiyonu, map(fonksiyon, array) -> Sonucu bir fonksiyondur.
def my_map(func, arg_list):         # Parametrelerden biri fonksiyon (yeterli) - Higher Order 
    result = []
    for i in arg_list:
        result.append(func(i))
    return result                   # Fonksiyon değil, değer döndürüyor.

squares = my_map(square, [1, 2, 3, 4, 5])   # square fonksiyonu yukarıda tanımlanmıştı.
# square fonksiyonunu argüman olarak verirken parantez kullanmıyoruz!!! Çalışmasını istemiyoruz.
print(squares)


def logger(msg):                # (Closure)
    def log_message():
        print("Log:", msg)
    return log_message          # Geriye fonksiyon döndürüyor. - Higher Order

log_hi = logger("Hi!")          # Fonksiyon argüman aldı ve geriye fonksiyon döndürdü.
log_hi()                        # Döndürülen fonksiyon çalıştırılabiliyor.

def html_tag(tag):  
    def wrap_text(msg):         # Bu sefer iç fonksiyonumuz da argüman alıyor.
        print("<{0}>{1}</{0}>".format(tag, msg))    # tag -> Outer fonksiyondan gelen "free variable"dır.
    return wrap_text

print_h1 = html_tag("h1")
print(print_h1)                 # Çıktı: <function html_tag.<locals>.wrap_text at 0x000001F5CEE7DD00>
print_h1("Test Headline!")      