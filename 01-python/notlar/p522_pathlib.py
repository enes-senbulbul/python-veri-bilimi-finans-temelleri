from pathlib import Path

aktif_dizin = Path.cwd()        # Current Working Dir'i nesne olarak almak
print(aktif_dizin)              
# Çıktı: C:\Users\enes\Desktop\...\python-veri-bilimi-finans-temelleri\01-python
print(repr(aktif_dizin))
# Çıktı: WindowsPath('C:\Users\enes\Desktop\...\python-veri-bilimi-finans-temelleri\01-python')

# Platform bağımsız Path birleştirme -> "/" bölme operatörü pathlib nesnelerinde özel olarak override 
# edilmiştir. Güvenli şekilde dosya path'i birleştirebiliriz.
hedef_dosya = aktif_dizin / "ayarlar" / "config.json"
print(f"Oluşan Yol:         {hedef_dosya}")
print(f"Dosya Adı:          {hedef_dosya.name}")
print(f"Dosya Uzantısı:     {hedef_dosya.suffix}")
print(f"Bulunduğu Klasör:   {hedef_dosya.parent.name}")
print(f"Dosya var mı?:      {hedef_dosya.exists()}")

# Oluşan Yol:         C:\Users\enes\Desktop\...\01-python\ayarlar\config.json
# Dosya Adı:          config.json
# Dosya Uzantısı:     .json
# Bulunduğu Klasör:   ayarlar
# Dosya var mı?:      False