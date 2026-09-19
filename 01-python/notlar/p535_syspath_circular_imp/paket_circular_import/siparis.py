# from .musteri import musteri_bilgisi -> CIRCULAR IMPORT HATASI

def siparis_olustur(isim, urun_adi):

    from .musteri import musteri_bilgisi    
    # Çözüm: fonksiyon içinde 'local' olarak import satırı yazılmalı
    # Bu sayede bu import daha sonra 'runtime' esnasında gerçekleşmeli

    bilgi = musteri_bilgisi(isim)
    return f"Fatura Kesildi: {bilgi} | Satın Alınan: {urun_adi}"