from collections import defaultdict, namedtuple, Counter


# --- Counter: Frekans Histogramı ---
veri_seti = [
    "elektronik", "giyim", "elektronik", "kitap", "giyim", 
    "elektronik", "kozmetik", "kitap", "elektronik", "giyim"
]

frekans = Counter(veri_seti)
print("En çok tekrar eden:", frekans.most_common(1))    # İçini boş bırakırsak hepsinin kaç defa tekrar ettiğini verir.
# Çıktı: En çok tekrar eden: [('elektronik', 4)]

c1 = Counter(a=3, b=1)
c2 = Counter(a=1, b=2, c=4)
print("Frekans toplamı: ", c1 + c2)     # Birbiriyle aritmetik işlemlere girebiliyor. 
# Çıktı: Frekans toplamı:  Counter({'a': 4, 'c': 4, 'b': 3})


# --- defaultdict: Eksik Anahtar Yönetimi ---
sozluk = {}
try: 
    sozluk["meyveler"].extend(["elma", "armut"])
except KeyError as anahtar:
    print(f"Hata: {anahtar} anahtarı bulunamadı.")

def_sozluk = defaultdict(list)      # Varsayılan tipi boş liste'dir. 
def_sozluk["meyveler"].extend(["elma", "armut"])
print("Gruplanmış Veri:", dict(def_sozluk))


# --- namedtuple: Hafif Veri Taşıyıcısı ---
Vektor = namedtuple("Vektor", ["x", "y", "z"])  # Yeni bir sınıf oluşturuyoruz.
v1 = Vektor(2, 3, 5)
print("Z bileşeni:", v1.z)

v1_sozluk = v1._asdict()    # Gerektiğinde sözlüğe çevirebiliyoruz.
print("v1 sözlük olarak:", v1_sozluk)


# Kod Uygulama - Verileri grupla + Hangi sensör kaç ölçüm yaptı ölç
sensor_verileri = [("T1", 22.5), ("P1", 1013), ("T1", 23.1), ("T2", 19.8), ("P1", 1012)]

okumalar = defaultdict(list)
sensor_sayaci = Counter()

for sensor_id, okunan_deger in sensor_verileri:
    okumalar[sensor_id].append(okunan_deger)    # Ölçümleri sensörlere ayrıştırıyoruz.
    sensor_sayaci[sensor_id] += 1               # Sensör'ün frekansını 1 arttırıyoruz.

print("T1 Ölçümleri:", okumalar["T1"])
print("Ölçüm Sayıları", sensor_sayaci.most_common())
# Çıktı:
# T1 Ölçümleri: [22.5, 23.1]
# Ölçüm Sayıları [('T1', 2), ('P1', 2), ('T2', 1)]