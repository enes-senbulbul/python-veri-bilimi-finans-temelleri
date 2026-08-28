cd notlar/p111-ornek-proje

uv venv # pin edilen 3.12'yi kullanarak sanal ortamı oluşturur.

.venv\Scripts\activate # Sanal ortamı aktive et (uv dışı komutlar için)
uv pip install rich # İzolasyonu test et: venv içine paket kur

uv run python -c "from importlib.metadata import version; print(version('rich'))"    
# venv aktifken paketi doğrula   # venv aktifken paketi doğrula

deactivate          # Sanal ortamdan çık
uv run python -c "from importlib.metadata import version; print(version('rich'))" 
# Venv dışındayken komut hata verir.