# Üç tane önemli Python standart library modülünü bu dosyada çalışacağız bakalım
# 1 - math  ->  bilimsel fonksiyonlar ve sabitler
# 2 - os    ->  dosya, klasör(dizin) işlemleri 
# 3 - sys   ->  CLI ile iletişim

# --- SYS ---
import sys

print("\n--- 1. 'sys' sabitleri ---".upper())
print("Python sürümü:", sys.version)
print("OS/Platform bilgisi:", sys.platform)
print("Python Okuyucusunun Path'i", sys.executable)
print("Python'un modül aradığı klasörler:", sys.path)       # Listeye .append ile modül yolunu ekliyebiliyoruz.


print("\n--- 2. 'sys' Terminalden Gelen Argümanları Okuma ---".upper())
print("Yazdığın şeyler: ", sys.argv[1:])
# Kodu terminalden python kod.py Ahmet Mehmet Ayşe şeklinde çalıştırdığımızda 
# kod.py -> sys.argv[0]
# Ahmet -> sys.argv[1]
# Mehmet -> sys.argv[2]
# Ayşe -> sys.argv[3]

print("\n--- 3. 'sys' Yüklenmiş Modülleri Görme ---".upper())
print("'sys' modülü yüklü mü:", "sys" in sys.modules)
print("'math' modülü yüklü mü:", "math" in sys.modules)