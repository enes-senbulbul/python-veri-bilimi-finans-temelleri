# VERİ MÜHENDİSLİĞİ & API TEMELLERİ

## İlerleme

  - 0.1 Web Temelleri
    - HTTP protokolü temelleri (istek/yanıt, status code, header)
    - JSON/XML veri formatları ve serileştirme
- [ ] BÖLÜM 1: API Tüketimi
  - 1.1 REST API Kavramları
    - REST mimarisi ilkeleri ve endpoint tasarımı
    - Kimlik doğrulama yöntemleri (API key, OAuth temelleri)
    - Rate limiting, sayfalama (pagination) ve toplu (bulk) istek stratejileri
  - 1.2 Python ile API İstemcisi Yazma
    - requests/httpx ile HTTP istekleri yapma
    - Yanıt doğrulama, hata kodları ve yeniden deneme (retry) mantığı
    - Zaman aşımı (timeout) ve üstel geri çekilme (exponential backoff)
- [ ] BÖLÜM 2: Otomasyon ve Zamanlama
  - 2.1 Otomatik Çalıştırma
    - Zamanlanmış görevler (cron / sistem zamanlayıcısı) temel kavramı
    - İş akışı orkestrasyonu (Airflow/Prefect) temel kavramları
    - İdempotentlik (idempotency) — aynı işi güvenle tekrar çalıştırabilme
  - 2.2 Hata Toleransı
    - Kısmi hata / yeniden başlatma (checkpoint) stratejileri
    - Veri kaynağı kullanılamazlığı (downtime) senaryolarına dayanıklılık
- [ ] BÖLÜM 3: Veri Kalitesi ve Doğrulama
  - 3.1 Giriş Verisi Doğrulama
    - Şema doğrulama (pydantic ile veri modelleme)
    - Eksik veri, tip uyuşmazlığı ve aykırı değer tespiti
    - Veri kaynağının veriyi sonradan revize/güncelleyebileceği farkındalığı
