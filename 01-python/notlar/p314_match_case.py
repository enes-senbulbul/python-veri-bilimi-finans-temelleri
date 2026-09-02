# match-case -> switch-case ama DAHA İYİSİ

# 1. Basit Değer Eşleme: klasik switch-case'in yapabildiği şey
def http_durum_kodu_isle(kod):
    match kod:
        case 200:   return "Başarılı: İşlem sorunsuz tamamlandı."   
        case 404:   return "Hata: Aranan sayfa veya kaynak bulunamadı."
        case 500:   return "Kritik Hata: Sunucu tarafında bir sorun oluştu."
        case _:     return "Bilinmeyen bir durum kodu girdiniz."
    # case'lerin sonuna break yazmamıza gerek yok. Eşleme sağlanınca kendi çıkıyor.
        
print(http_durum_kodu_isle(200))

# 2. Değişken Eşleme (Variable Binding): 
# Gelen veriyi eşleştirdiği anda değişkene atayarak yakalama işlemidir. 
# Yakalanan değer case bloğunun içinde doğrudan kullanılabilir.
# case_:(wildcard) yapısı yerine gelen verinin ne olduğunu bilmek ve ekrana 
# yazdırmak/kullanmak istediğimizde çok işe yarar.
def yon_komutu_calistir(komut):
    match komut:
        case "Kuzey"|"Güney"|"Doğu"|"Batı":
            print(f"Karakter {komut} yönüne ilerliyor.")
        case hatali_girdi:  # Gelen değer yukarıdakilere uymazsa bu değişkene atanır.
            print(f"Hata: '{hatali_girdi}' geçerli bir yön komutu değildir!") 

yon_komutu_calistir("Kuzey")
yon_komutu_calistir("Yukarı") 


# 3. Koleksiyon Eşleme (Sequence Matching / Unpacking):
# Liste/Tuple gibi veri yapılarının hem uzunluğunu kontrol eder hem de eşleşme 
# sağlanırsa içindeki verileri dışarı çıkarıp (unpacking) değişkenlere atar.
def kullanici_kaydi_olustur(veri):
    match veri:
        case [isim]:    
            print(f"Kullanıcı oluşturuldu: {isim} (Soyisim belirtilmedi)")
        case [isim, soyisim]:
            print(f"Kullanıcı oluşturuldu: {isim} {soyisim}")
        case [isim, soyisim, yas]:
            print(f"Kullanıcı oluşturuldu: {isim} {soyisim}, Yaş: {yas}")
        case _:
            print("Geçersiz veri formatı. Lütfen bilgileri kontrol edin.")

kullanici_kaydi_olustur("Ali") # Bu geçersiz oluyor. Sadece isim de liste dahilinde
kullanici_kaydi_olustur(["Ali"])
kullanici_kaydi_olustur(["Ayşe", "Yılmaz", 25])


# 4. Guard (Koruyucu) Kullanımı
# Eşleşme sağlandıktan sonra yapıya ekstra bir mantıksal koşul eklememizi sağlar.
# Eğer bu koşul sağlanmazsa, o case bloğu pas geçilir ve sonrakine bakılır.
def sicaklik_uyarisi(olcum):
    match olcum:
        case (derece, "C") if derece>30:    # Hem formata uygun, hem de >30 şartı (Guard) var.
            print(f"Uyarı: Hava çok sıcak! ({derece}°C)")
        case (derece, "C") if derece<5:
            print(f"Uyarı: Don tehlikesi! ({derece}°C)")
        case (derece, "C"):
            print(f"Hava sıcaklığı normal seviyelerde. ({derece}°C)")
        case _:
            print("Lütfen ölçümü (derece, 'C') formatında giriniz.")

sicaklik_uyarisi((35, "C"))
sicaklik_uyarisi((20, "C"))


# Pratik - Noktanın kaç boyutlu düzlemde olduğunu bulma
def konum_bulucu(nokta):
    match nokta:
        case (0, 0) | [0, 0] | (0, 0, 0) | [0, 0, 0]:
            print("Nokta orijinde")
        case (x,y) | [x,y]:
            print(f"2D Nokta: x={x}, y={y}")
        case (x,y,z) | [x,y,z]:
            print(f"2D Nokta: x={x}, y={y}, z={z}")
        case _: 
            print("Gecersiz format")

konum_bulucu((0, 0))       # Çıktı: Nokta orijinde
konum_bulucu([5, 10])      # Çıktı: 2D Nokta: x=5, y=10
konum_bulucu((1, 2, 3))


# Pratik - match-case'in tüm özellikleri bir arada
def komut_islet(komut_girdisi):
    match komut_girdisi:
        case "cikis" | "kapat":     # 1. Basit değer eşleme
            return "Sistem kapatılıyor..."
        case ["yukle", dosya_adi]:  # 3. Liste unpacking 
            return f"{dosya_adi} yukleniyor..."     # 2. Değişken Eşleme
        case ["boya", nesne, renk] if renk == "kirmizi":    # 4. Guard Kullanımı
            return f"{nesne} KIRMIZIYA boyanıyor! (Özel durum)"
        case ["boya", nesne, renk]:
            return f"{nesne} {renk} rengine boyanıyor."
        case _:
            return "Bilinmeyen komut formatı!"

print(komut_islet("cikis"))
print(komut_islet(["yukle", "veri.csv"]))
print(komut_islet(["boya", "duvar", "kirmizi"]))
print(komut_islet(["boya", "kapi", "mavi"]))
print(komut_islet("rastgele_metin"))