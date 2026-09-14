# PARENT CLASS
class VeriTabani:                                   

    def __init__(self, baglanti_dizgesi):
        self.baglanti_dizgesi = baglanti_dizgesi
        self.bagli_mi = False

    # Bu metot alt sınıflarda da sınıfa özel şekilde tanımlanmalı ve bunu ezmeli.
    def baglan(self):
        raise NotImplementedError("Bu metot alt sınıflarda o sınıfa özgü şekilde tanımlanmalı!")

    def baglantiyi_kes(self):
        self.bagli_mi = False
        return "Bağlantı kesildi."

# DERIVED CLASS 1
class PostgresDB(VeriTabani):                       

    def __init__(self, baglanti_dizgesi, sema):
        # Parent class'ın __init__ metodunu super() referansı ile çağırıyoruz.
        super().__init__(baglanti_dizgesi)      # self'i kendisi ekliyor. 
        # Java'da direkt super(baglanti_dizgesi) yaziyorduk çok rahattı
        self.sema = sema

    def baglan(self):               # Postgres nesnelerine özel baglan() metodu - Polymorphism 
        self.bagli_mi = True
        return f"Postgres veritabanına ({self.sema} şeması) TCP üzerinden bağlanıldı."

# DERIVED CLASS 2
class MongoDb(VeriTabani):                          

    # Özel bir __init__ tanımlamadığımız için parent'in __init__ metodunu otomatik kullanır.
    # MRO - Method Resolution Order 

    def baglan(self):
        self.bagli_mi = True
        return f"MongoDb veritabanına HTTP/REST üzerinden bağlanıldı."


# --- Sınıfları kullanmak ---

# Polymorphism Uygulaması 
database_listesi = [PostgresDB("localhost:5432", "public"), MongoDb("localhost:27017")]

for database in database_listesi:
    print(database.baglan())
# Çıktı:
# Postgres veritabanına (public şeması) TCP üzerinden bağlanıldı.
# MongoDb veritabanına HTTP/REST üzerinden bağlanıldı.

print("İlk database nesnesi, PostgresDB mi? :", isinstance(database_listesi[0], PostgresDB))
print("İlk database nesnesi, VeriTabani mi? :", isinstance(database_listesi[0], VeriTabani))
# İkisi de 'True'. Bir Postgres aynı zamanda bir VeriTabani nesnesidir.

print("MongoDb sınıfı VeriTabani'ndan mı türemiş? :", issubclass(MongoDb, VeriTabani))  # Çıktı: True