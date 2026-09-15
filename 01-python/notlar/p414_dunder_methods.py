# dunder methods -> Double Underscore Methods 
# 1) __str__    son kullanıcı için string temsili
# 2) __repr__   geliştirici için esas string temsili
# 3) __eq__     eşitlik ""==" tanımlaması, aynı lokasyondaki aynı nesne olmaksızın value aynıysa 

class APIIstegiKotu:

    # Constructor for Initialization 
    def __init__(self, endpoint, method="GET"):
            self.endpoint = endpoint 
            self.method = method


class APIIstegi:

    # Constructor for Initialization 
    def __init__(self, endpoint, method="GET"):
        self.endpoint = endpoint 
        self.method = method

    # Okunaklı, kullanıcı dostu metin formatı
    def __str__(self):
        return f"[{self.method}] {self.endpoint}"

    # Geliştirici için resmi (umambiguous) format
    def __repr__(self):
        return f"APIIstegi(endpoint='{self.endpoint}', method='{self.method}')"
        # İdeal olarak nesneyi yeniden yaratacak kodu döndürmeli

    # Değer eşitliği (value equality) Kontrolü
    def __eq__(self, other):
        # Diğer nesne aynı tipte değilse zaten direkt eşit değiller 
        if not isinstance(other, APIIstegi):
            return False

        esitlik = (self.endpoint == other.endpoint) and (self.method == other.method)
        return esitlik 


# Aralarındaki Farkı Görelim Bakalım

istek1_kotu = APIIstegiKotu("/users", "GET")
istek1 = APIIstegi("/users", "GET")

# __str__ tanımlanmışsa direkt onu kullanır. İkinci sınıfın nesnesi istek1 öyle yapıyor.
print(istek1_kotu)      # Çıktı: <__main__.APIIstegiKotu object at 0x0000029C7EF770E0>
print(istek1)           # Çıktı: [GET] /users

print(str(istek1_kotu)) # Yine lokasyon gösterir çıktı olarak
print(str(istek1))      # Çıktı: [GET] /users
print(repr(istek1))     # Çıktı: APIIstegi(endpoint='/users', method='GET')

istek2_kotu = APIIstegiKotu("/users", "GET")
istek2 = APIIstegi("/users", "GET")

print(istek1_kotu == istek2_kotu)       # Çıktı: False
print(istek1 == istek2)                 # Çıktı: True
print(istek1 is istek2)                 # Çıktı: False 