_gizli_stok_veritabani = {
    101:    {"ad":"Laptop",     "fiyat": 25_000,    "stok":5},
    102:    {"ad":"Mouse",      "fiyat": 500,       "stok":0},
    103:    {"ad":"Klavye",     "fiyat": 1500,      "stok":12}
}

def urun_listesini_goster() -> list[str]:
    return [f"kod:{kod} | {urun["ad"]} | {urun["fiyat"]} TL" for kod, urun in _gizli_stok_veritabani.items()]

def urun_sorgula(urun_id) -> dict:
    if urun_id not in _gizli_stok_veritabani:
        raise ValueError(f"Hata: {urun_id} ID'li ürün bulunamadı!")
    return _gizli_stok_veritabani[urun_id]

def stok_kontrol(urun_id, adet):
    urun = urun_sorgula(urun_id)
    if urun["stok"] < adet:
        raise ValueError(f"Stok yetersiz :( {urun["ad"]} ürününden sadece {urun["stok"]} tane kalmış.") 
    return True

def stok_dus(urun_id, adet):
    urun = urun_sorgula(urun_id)
    stok_once = urun["stok"]
    urun["stok"] -= adet
    print(f"Stok ({urun["ad"]}): {stok_once} -> {urun["stok"]}")
    return True