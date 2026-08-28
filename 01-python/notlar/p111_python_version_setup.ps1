# --- Bir projede python sürümü sabitlemek ---
cd notlar
mkdir p111-ornek-proje
cd p111-ornek-proje

uv python pin 3.12     # Proje'yi 3.12'ye sabitle (.python-version oluşur)
cat .python-version     # Hangi sürümde çalıştığını sorgula 

uv run python --version

python --version    # Bilgisayarda esas kurulu olan python sürümünü gösterir --> 3.13