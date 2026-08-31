# if-elif-else 
P = 14.5
if P <= 10:
    print("Düşük")
elif 10 < P <=20:           # Python'da eşitsizliği ikiye ayırmamıza gerek yok
    print("Normal")
else: 
    print("Yüksek")


# Truthiness 
hata_logu = []              # Boş collectionlar falsy'dir. 
if not hata_logu:
    print("Sistem stabil, hata yok")
else:
    print("Hata var")
