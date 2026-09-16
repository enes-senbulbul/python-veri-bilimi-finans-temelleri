# Bölme işlemi için güvenli bir fonksiyon tanımlayalım.
def guvenli_bolme(bolunen, bolen):
    try:
        sonuc = bolunen / bolen     # Riskli işlemi try bloğu içinde gerçekleştiriyoruz. 

    # Farklı istisnalar için ayrı senaryolar planlayabiliriz.
    except ZeroDivisionError as hata_mesaji:
        print(f"Hata yakalandı: Sıfıra bölme yapılamaz! ({hata_mesaji})")
    except TypeError:
        print("Hata yakalandı: Lütfen sadece sayı giriniz.")

    # 'try' bloğu hata olmadan çalışırsa 'else' bloğu da çalışır.
    else:
        print(f"İşlem başarılı, sonuç: {sonuc}")

    # Her durumda -hata olsun/olmasın- bu blok çalışır.
    finally:
        print("Hesaplama bloğu sonlandı.")


guvenli_bolme(10, 2)
# İşlem başarılı, sonuç: 5.0
# Hesaplama bloğu sonlandı.

guvenli_bolme(10, 0)
# Hata yakalandı: Sıfıra bölme yapılamaz! (division by zero)
# Hesaplama bloğu sonlandı.

guvenli_bolme(10, "a")
# Hata yakalandı: Lütfen sadece sayı giriniz.
# Hesaplama bloğu sonlandı.