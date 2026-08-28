cd notlar/p111-ornek-proje
.venv/Scripts/activate

uv init --no-readme     # pyproject.toml ve uv.lock'u oluşturur.

uv add pandas requests  # proje bağımlılıklarını ekle
uv add --dev pytest     # Sadece geliştirme ortamı için 

cat pyproject.toml      # içeriğine bak
# meta verileri, proje dosyası ismi her şey var.

uv pip freeze > requirements.txt    # Klasik formata da aktar
cat requirements.txt    # içeriğine bak ve karşılaştır.