# p534 konusu için paket örneği: 
print(f"[Sistem] 'p534_ornek_package' paketi yükleniyor...")

# Paket seviyesinde global konfigürasyon değişkenleri bu en genel __init__'e yazılır.
PAKET_VERSIYON = "2.1.0"
SISTEM_DURUM = "Aktif"


# alt paketlerden/modüllerden sadece dışarı açmak istediklerimizi burada temize çekiyoruz.

# --- VİTRİN (FACADE) --- 
# (Dışarı Sergilenecekler) - Esas p534 dosyamızda import * dediğimizde sadece bunlar gönderilecek
from .alt_paket_kullanici.profil import Kullanici           # Relative Import 
__all__ = ["Kullanici", "PAKET_VERSIYON"]