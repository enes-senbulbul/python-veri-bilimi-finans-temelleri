if __name__ == "__main__":      
# Daha sonra bu p532 dosyasını da p533'e import ettiğimde orada şu alttakilerin çalışmasını istemiyorum. 

    import p531_module as p531    # Bu .py dosyasını baştan sona çalıştırır.

    # O dosyadaki dışarıda bırakılan math.sqrt(25) vs. burada da başlangıçta aynen çalışıyor.
    # Lakin __main__ içindeki işlemler gerçekleşmiyor.

    print("p531 modül mü? script mi? ", p531.__name__)

    # Şu ana kadar çıktımız: 
    # 5.0
    # 25'in kökünü nası alim şimdi?
    # 5.0   
    # 5                                                     -> p531 tamamı (__main__ hariç)
    # p531 modül mü? script mi?  p531_module_package        -> p532 bu satıra kadar

    p531.ana_uygulama()     # Çıktı: Sistem başlatıldı
    print(p531.metin_formatla("p531'in fonksiyonlarını ve değişkenlerini (nesnelerini) kullanabiliyoruz."))
    print(p531.bilgiler)    # Çıktı: {'ad': 'Ali', 'yaş': 34, 'sigorta': True}



# --- Buradan itibaren yazılan kodlar p533 için ---

def merhaba(isim): print("Merhaba,", isim)
def gorusuruz(isim): print("Tekrardan görüşmek üzere,", isim)
def _gizli_fonksiyon(): print("Sadece p532'ye ait bir fonksiyon. __all__ içinde olmasa bile import * ile aktarılmaz.")
def hal_hatir_sor(): print("Nasıl gidiyor abi? Neler yaptın bu haftasonu?")
def borc_iste(miktar): print(f"Abi bi {miktar} borç verebilecen mi bana? Sana ben bi ara(?) öderim")

__all__ = ["merhaba", "hal_hatir_sor", "gorusuruz"]