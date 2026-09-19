from .siparis import siparis_olustur    # Global import 

def musteri_bilgisi(isim):
    return f"Kayıtlı Müşteri ({isim})"

def alisveris_yap(isim, urun_adi):
    print(f"[{isim}] alışveriş sepetini onaylıyor...")
    return siparis_olustur(isim, urun_adi)

# -- Interpreting ---
# Python musteri.py'i okumaya başlar. İlk satırdaki global import yüzünden siparis.py'ye zıplar.
# siparis.py'de siparis_olustur fonksiyonunu görür ancak içindeki kodları (ve yerel importu) çalıştırmaz.
# siparis.py biter ve musteri.py'te geri döner. Kalan musteri_bilgisi ve alisveris_yap fonksiyonlarını okuyup belleğe yazar.

# --- Runtime ---
# alisveris_yap fonksiyonu çağrılır ve o da siparis_olustur'u tetikler.
# kod ilk kez siparis_olustur'un içine girer ve yerel import satırına ulaşır.
# Python belleğe bakar, musteri.py zaten okunduğu için bellekte hazır beklemektedir.
# Python dosyayı yeniden okumaz, bellekteki hazır fonksiyonu o anki haliyle anında çekip
# kullanır ve işlem başarıyla tamamlanır.

# İmport'lar farklı aşamalarda gerçekleştiği için çakışma yaşanmaz.