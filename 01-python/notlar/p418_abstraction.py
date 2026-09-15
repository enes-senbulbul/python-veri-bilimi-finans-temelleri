from abc import ABC, abstractmethod

# Soyut Sınıf: Direkt bu sınıftan nesne yaratamıyoruz.
class OdemeSaglayicisi(ABC):    # 'abstract' keywordü yok Java'daki gibi.

    @abstractmethod                         # Soyut methodların içi ya boş bırakılır (pass) ya da docstring yazılır.
    def odeme_yap(self, miktar: float):     # Her alt sınıfın kendi odeme_yap metodu olmak zorundadır.
        pass 

    @abstractmethod
    def iade_et(self, islem_id: str):
        pass


# Alt Sınıf 1: Doğru tanımlanan alt sınıf
class StripeOdeme(OdemeSaglayicisi):
    # Soyut sınıfın tüm soyut metotları override ediyoruz.
    def odeme_yap(self, miktar: float):
        return f"Stripe üzerinden {miktar} TL çekildi."
    def iade_et(self, islem_id: str):
        return f"Stripe işlemi ({islem_id}) iade edildi."


# Alt Sınıf 2: Hatalı alt sınıf
class IyzicoOdeme(OdemeSaglayicisi):
    def odeme_yap(self, miktar: float):
        return f"Iyzico üzerinden {miktar} TL çekildi."
    # iade_et metodu yazmayı unuttuk diyelim.


# --- Sınıfları Test Ettiğimizde ---

# Doğru sınıf sorunsuz çalışır.
stripe = StripeOdeme()
print(stripe.odeme_yap(100.0))      # Çıktı: Stripe üzerinden 100.0 TL çekildi.

# Hatalı sınıftan nesne üretmeye çalıştığımızda TypeError hatası verir. "fast-fail" 
# prensibi ile hatalı nesnenin üretilmesine olanak bırakmadan erkenden çöker.
try: 
    iyzico = IyzicoOdeme()
except TypeError as hata_mesaji:
    print(f"Hata yakalandı: {hata_mesaji}") 
# Çıktı: Hata yakalandı: Can't instantiate abstract class IyzicoOdeme without an
# implementation for abstract method 'iade_et'