print("Döngü başlıyor...")

for i in range(1, 4):
    # Her iterasyonda (adımda) kod burada duracak.
    # Pdb konsolunda 'i' yazarak mevcut değeri görebilir, 'n' ile bir sonraki
    # adıma, 's' ile bir fonksiyon çağrısının içine, 'c' ile devam edebilirsiniz.
    breakpoint()
    hesaplama = i * 10
print("Döngü bitti.")

# VSCode'un da görsel debugging paneli var ayrıca,
# Yukarıda step over, step into, step out butonları var. Pdb ve harflerle uğraşmaya gerek yok.
# Herhangi bir andaki(breakpoint) local, global değişkenleri, call stack içeriğini görebiliyoruz.
# sol taraftaki kırmızı noktalar breakpointmiş, kodun içine yazmaktan kurtarıyo bu da