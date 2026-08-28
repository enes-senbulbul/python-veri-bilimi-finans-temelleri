# --- uv aracını Windows sisteme kurmak için ---
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"

uv --version    # uv'nin kurulu olduğunu doğrula

uv python install 3.12      # Belirli bir Python sürümü kurma
uv python install 3.11

uv python list  # Yüklü python sürümlerini listele
