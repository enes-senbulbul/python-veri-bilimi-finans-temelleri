from dataclasses import dataclass, field 
from typing import List     # Amaç: list yerine geriye uyumluluk için List kullanabilmek

@dataclass 
class SunucuYapilandirması:
    # Type Hints zorunludur. 
    ip_adresi: str
    port: int
    aktif: bool = True 


# Nesneleri oluşturabiliriz /  __init__ otomatik olarak var. 
config1 = SunucuYapilandirması("192.168.1.10", 8080)
config2 = SunucuYapilandirması("192.168.1.10", 8080)

# Yazdırabiliriz / __repr__ de var.
print(config1)              # Çıktı: SunucuYapilandirması(ip_adresi='192.168.1.10', port=8080, aktif=True)

# Değer eşitliği kontrol edebiliriz / __eq__ de tanımlanmış.
print(config1 == config2)   # Çıktı: True


# Mutable Type'ların varsayılan değeri doğrudan atanmaz. Yoksa aynı nesneyi paylaşırlar.
@dataclass
class APIKullanicisi:
    kullanici_adi: str
  # yetkiler: List[str] = []    -> Yanlış. Zaten derleme anında dataclasses modülü de kasıtlı olarak engelliyor. ValueError
    yetkiler: List[str] = field(default_factory=list)
    # Doğru yöntem: Her yeni nesne için yeni bir liste üretecek 'factory' fonksiyonunu default değer olarak ayarlamak

user = APIKullanicisi("admin_ahmet")
user.yetkiler.append("READ")
print(user)
# Çıktı: APIKullanicisi(kullanici_adi='admin_ahmet', yetkiler=['READ'])