# 1. Python Programlama Temelleri

## İlerleme

- [x] BÖLÜM 1: Kurulum ve Geliştirme Ortamı
  - 1.1 Ortam Kurulumu
    - Python yorumlayıcısı kurulumu ve sürüm yönetimi (pyenv/uv)
    - Sanal ortamlar (venv) ve bağımlılık izolasyonu
    - Paket yöneticisi (pip/uv) ve requirements.txt / pyproject.toml
    - Kod editörü kurulumu ve temel debugger kullanımı

- [x] BÖLÜM 2: Temel Sözdizimi ve Veri Tipleri
  - 2.1 Temel Veri Tipleri
    - Sayısal tipler (int, float, complex) ve aritmetik
    - Metin tipi (str) ve temel string metodları
    - Boolean, None ve doğruluk değeri (truthiness) kuralları
    - Tip dönüşümü (casting) ve dinamik tipleme kavramı
  - 2.2 Koleksiyon Tipleri
    - Liste (list) — oluşturma, indeksleme, dilimleme (slicing)
    - Demet (tuple) ve değişmezlik (immutability) kavramı
    - Sözlük (dict) — anahtar-değer yapıları ve metodları
    - Küme (set) ve küme işlemleri
    - List/dict/set comprehension

- [ ] BÖLÜM 3: Kontrol Akışı ve Fonksiyonlar
  - 3.1 Kontrol Yapıları
    - Koşullu ifadeler (if/elif/else)
    - Döngüler (for, while) ve döngü kontrol ifadeleri (break/continue)
    - Yineleyiciler (iterators) ve üreteçler (generators)
  - 3.2 Fonksiyonlar
    - Fonksiyon tanımı, parametreler ve varsayılan değerler
    - *args, **kwargs ve esnek parametre yapıları
    - Kapsam (scope) kuralları ve closures
    - Lambda ifadeleri ve fonksiyonel araçlar (map/filter/reduce)
    - Dekoratörler (decorators)

- [ ] BÖLÜM 4: Nesne Yönelimli Programlama
  - 4.1 OOP Temelleri
    - Sınıf (class) tanımı, __init__ ve örneklem
    - Örnek/sınıf/statik metodlar ve öznitelikler
    - Kalıtım (inheritance) ve çok biçimlilik (polymorphism)
    - Özel metodlar (dunder methods: __str__, __repr__, __eq__)
    - Kompozisyon vs kalıtım kararı
    - Dataclasses ve tip ipuçları (type hints) ile veri modelleme

- [ ] BÖLÜM 5: Hata Yönetimi, Dosya/IO ve Standart Kütüphane
  - 5.1 Hata Yönetimi
    - try/except/finally ve istisna (exception) hiyerarşisi
    - Özel istisna sınıfları tanımlama
    - Context manager'lar (with ifadesi) ve kaynak yönetimi
  - 5.2 Dosya ve Veri Formatları
    - Dosya okuma/yazma (metin, CSV, JSON)
    - Yol (path) yönetimi (pathlib)
  - 5.3 Standart Kütüphane ve Modülerlik
    - Modül/paket yapısı ve import sistemi
    - datetime ve zaman damgası işlemleri
    - collections modülü (defaultdict, namedtuple, Counter)
    - logging modülü ile günlükleme

- [ ] BÖLÜM 6: Test Yazma ve Kod Kalitesi
  - 6.1 Test Yazma
    - Birim test kavramı ve pytest ile test yazma
    - Fixture'lar ve mock kullanımı
  - 6.2 Kod Kalitesi
    - Tip ipuçları (typing modülü) ve statik analiz (mypy)
    - Kod biçimlendirme ve linting (ruff/black)
    - Docstring standartları ve kod dokümantasyonu
