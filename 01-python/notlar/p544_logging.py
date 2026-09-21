import logging
import sys


logging.getLogger().handlers.clear()    # Root ayarların üst üste binmemesi için handlerları sıfırlanma
logger = logging.getLogger(__name__)    # Modülün kendi adına özgü bir logger oluşturmak

logging.basicConfig(
    level=logging.INFO,     # Bu eşiğin (<20) altındakiler yok sayılır.
    format= "%(asctime)s | %(levelname)s | [%(name)s %(message)s]",     # Çıktı Şablonu
    datefmt="%H:%M:%S", 
    stream=sys.stdout,
    force=True              # Jupyter/Colab veya test ortamlarında eski ayarları ezmek için
)

# Log oluşturma denemeleri
logging.debug("Bu debug mesajı görünmeyecek çünkü eşiğin altında.")
logging.info("Veritabanı bağlantısı kuruldu.")
logging.warning("Disk alanı %15 seviyesinde.")
logging.error("Sorgu zaman aşımına uğradı.")
logging.critical("Bellek tükendi, süreç sonlanıyor!")
print("-"*30)

# İstisnaları loglarken hata ağacını (traceback) kaybetmemek kritik öneme sahipmiş. Nerede? hangi satırda? vs
try:
    sonuc = 1 / 0
except ZeroDivisionError:
    logger.exception("Matematiksel bir hata yakalandı") 

# Pratik
def matris_inverse(veri):
    logger.debug(f"Gelen ham veri: {veri}")     # Eşiğin altında olduğu için konsolu kirletmez.

    if not veri:
        logger.warning("Boş veri seti ile işlem yapılmaya çalışıldı, atlanıyor.")
        return None

    logger.info(f"{len(veri)} boyutlu matris işleniyor...")
    # Tabi tersini almak için kütüphane lazım 
    return "Başarılı Sonuç xd"

matris_inverse([])
matris_inverse([[1,1], [1,2]])