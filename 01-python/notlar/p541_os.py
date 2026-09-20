# Üç tane önemli Python standart library modülünü bu dosyada çalışacağız bakalım
# 1 - math  ->  bilimsel fonksiyonlar ve sabitler
# 2 - os    ->  dosya, klasör(dizin) işlemleri 
# 3 - sys   ->  CLI ile iletişim

# --- OS ---
import os

print("\n--- 1. 'os' sabitleri ---".upper())
print("İşletim sisteminin türü (Windows -> nt, Linux/MacOS -> posix):", os.name)
print("İşletim sisteminin platform bilgisi:", os.sys.platform)
print("Klasör ayırıcı karakter:", os.sep)
# os.linesep -> Satır sonu karakteri koymamıza yarar OS'e göre
# os.pathsep 
# os.curdir -> Güncel dizin (.)
# os.pardir -> (Parent) üst dizin (..) 


print("\n--- 2. 'os' Dosya ve Klasör Fonksiyonları ---".upper())
print("Güncel dizin'i döndürür:", os.getcwd())

print("Belirli bir dizinin içindeki dosyaları liste olarak döndürür.")
dosyalar = os.listdir("notlar/p536_dinamik_paket")
for i, dosya in enumerate(dosyalar, 1):
    print(i, dosya)

print("Klasörün varlığını kontrol eder:", os.path.exists("notlar/p536_dinamik_paket"))
print("Relative path?:", os.path.relpath("."))
print("Absolute path?:", os.path.abspath("."))
print("Dosya mı Klasör mü?:", os.path.isfile("notlar/p536_importlib.py"))
print("Dosya boyutu (byte):", os.path.getsize("notlar/p536_importlib.py"))
print("Environment Variables:", list(map(lambda dosya: os.path.basename(dosya), os.environ.get("PATH").split(os.pathsep))))


print("\n--- 3. 'os' Dosya Bilgileri ---".upper())
bilgiler = os.stat("notlar/p536_importlib.py")
print("Dosya boyutu:", bilgiler.st_size)
print("Son Erişim:", bilgiler.st_atime)
print("Son Değişiklik:", bilgiler.st_mtime)  
print("Son Metadata Değişikliği:", bilgiler.st_ctime)   # Çıktılar hep Epoch formatında


print("\n--- 4. 'os' Script içinde CLI Komutu Çalıştırmak ---".upper())
os.system("echo Merhaba")           # YERINE SUBPROCESS MODÜLÜ KULLANMALIYIZ.
os.system("ping google.com")