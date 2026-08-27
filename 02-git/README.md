# GİT & YAZILIM MÜHENDİSLİĞİ ARAÇLARI

## İlerleme

- [ ] BÖLÜM 1: Versiyon Kontrolü
  - 1.1 Git Temelleri
    - Git deposu oluşturma, commit, staging area kavramı
    - Branch (dal) oluşturma, birleştirme (merge) ve çakışma çözme
    - Uzak depo (remote) ile çalışma (push/pull/fetch)
    - .gitignore ve hassas veri/kimlik bilgisi yönetimi
  - 1.2 İşbirliği Akışları
    - Pull request / code review süreci
    - Commit mesajı standartları ve anlamlı geçmiş oluşturma
    - Git rebase vs merge stratejileri
- [ ] BÖLÜM 2: Proje Paketleme ve Bağımlılık Yönetimi
  - 2.1 Paketleme
    - pyproject.toml ile proje yapılandırma
    - Bağımlılık kilitleme (lock dosyaları) ve tekrarlanabilir kurulum
    - Komut satırı arayüzü (CLI) tasarımı (argparse/click/typer)
- [ ] BÖLÜM 3: Test, CI/CD ve Otomasyon
  - 3.1 Sürekli Entegrasyon
    - GitHub Actions ile otomatik test/lint pipeline'ı kurma
    - pre-commit hook'ları ile kod kalitesi otomasyonu
  - 3.2 Konteynerleştirme
    - Docker temel kavramlar (image, container, Dockerfile)
    - docker-compose ile çok-servisli ortam kurma (uygulama + veritabanı)
- [ ] BÖLÜM 4: Konfigürasyon, Gizli Bilgi ve Günlükleme Mimarisi
  - 4.1 Konfigürasyon Yönetimi
    - Ortam değişkenleri (.env) ve gizli anahtar (API key) yönetimi
    - Katmanlı konfigürasyon (dev/test/prod ayrımı)
  - 4.2 Gözlemlenebilirlik
    - Yapılandırılmış günlükleme (structured logging) tasarımı
    - Hata izleme ve uyarı (alerting) temelleri
- [ ] BÖLÜM 5: Açık Kaynak Proje Standartları
  - 5.1 Açık Kaynak Uygulamaları
    - Lisanslama (MIT/Apache/GPL) seçimi ve anlamları
    - README, CONTRIBUTING ve proje dokümantasyon yapısı
    - Sürüm etiketleme (semantic versioning) ve release süreci
