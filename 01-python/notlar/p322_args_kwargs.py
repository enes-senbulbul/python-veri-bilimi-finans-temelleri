# *args ile positional argümanları topluca alabilen fonksiyon tanımı
def ortalama_hesapla(*args):
    if not args:        # Boş tuple kontrolü, payda=0 tanımsızlığını önleme
        return 0
    return sum(args)/len(args)

print("Ortalama 1:", ortalama_hesapla(10,20,30))
print("Ortalama 2:", ortalama_hesapla(5,10,15,20,25))


# **kwargs ile keyword argümanları topluca alabilen fonksiyon tanımı
def model_ayarla(**kwargs):
    for ayar_adi, deger in kwargs.items():
        print(f"Konfigürasyon uygulandı: {ayar_adi} = {deger}")

model_ayarla(learning_rate=0.01, epochs=100, optimizer="adam")


# Packing ve Unpacking Ayrımı - Bunu komple kendim baştan yazdım :)
veri_seti = ["elma", "armut","elma","elma","armut", 1, 2, True]

def tepe_degeri_bulma(*args):       # Packing
    if not args:
        return None
    else:
        count = 1
        tepe_eleman = args[0]
        for eleman in args:
            if count < (sayi := args.count(eleman)):
                count = sayi
                tepe_eleman = eleman
        return count, tepe_eleman 

tekrar_sayisi, tepe_degeri = tepe_degeri_bulma(*veri_seti)  # Unpacking
print(f"{veri_seti} \nEn çok tekrar eden (Tepe Değeri): {tepe_degeri} \nTekrar sayısı: {tekrar_sayisi}")


# PEP8 Parametre Sırası -> standart, *args, default, **kwargs
def rapor_olustur(baslik, *veriler, **meta_bilgiler):
    print(f"--- {baslik.upper()} ---")
    toplam = sum(veriler)
    print(f"Toplam Veri Değeri: {toplam}")
    tarih = meta_bilgiler.get("tarih", "Belirtilmedi")
    print(f"Rapor Tarihi: {tarih}")

veriler = [100, 250, 50]
meta_data = dict(tarih="2023-10-01", yazar="Mehmet")
rapor_olustur("Satış Analizi",*veriler, **meta_data)    # Liste, dict Unpacking beraber