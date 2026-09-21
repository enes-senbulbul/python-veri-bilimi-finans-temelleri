import re

# 1. Arama, Eşleşme -> search, match
# 2. Tümünü Bulma -> findall, finditer
# 3. Değiştirme, Sansürleme -> sub
# 4. Bölme -> split 

# 1. Arama (search): Metnin neresinde olursa olsun pattern'e uyan ilk eşleşmeyi bulur.
# Regex patternleri hep ezbermiş 
metin = "Sipariş numaranız: 14592, kargoya verildi."
eslesme = re.search(r"\d+", metin)
print(f"Bulunan sayı: {eslesme.group()} | Başlangıç İndeksi: {eslesme.start()}")

# 2. Tümünü Bulma (findall): Eşleşen tüm sonuçları bir liste olarak döndürür.
metin = "Merhaba! Python 3.13 Regex öğrenmeye çalışıyorum..."
eslesmeler = re.findall(r"\w+", metin)
print(f"Kelimeler: {eslesmeler}")

# 3. Değiştirme (sub): Eşleşen kısımları başka bir metinle değiştirir.
telefon = "Tel: +90 545 123 11 22"
gizli_telefon = re.sub(r"\d{3} \d{2} \d{2}", "XXX XX XX", telefon)
print(f"Sansürlü tel num: {gizli_telefon}")

# 4. Bölme (split): Belirli bir örüntüye göre metni böler (str.split'in daha gelişmişi)
elemanlar = "Elma, Armut; Çilek | Kavun"
bolunmus_liste = re.split(r"[;,|]\s*", elemanlar)   
# [;,|]\s* -> İçerideki karakterlerden birisinden sonra boşluk varsa (ister bir tane, ister beş tane, ister hiç olmasın) hepsini dahil et."
print(f"Bölünmüş liste: {bolunmus_liste}")


# Eğer eşleşme bulunamazsa 'None' döndürürler. 
# re.IGNORECASE ile küçük/büyük harf duyarsız arama yapabiliyoruz.
# search tüm metin içinde arama yaparken match sadece en başı o pattern ile mi başlıyor kontrolü yapar.