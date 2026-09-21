import random 


random.seed(42)     # Script her çalıştırıldığında aynı sonuçlar generate edilir.
print(f"0.0-1-0 arasında rastgele float: {random.random()}")
print(f"a ve b arasında int, ikisi de dahil: {random.randint(1, 100)}")
print(f"a ve b arasında float: {random.uniform(1,100)}")
print(f"range içinden int: {random.randrange(1,100,5)}")

liste = ["Elma", "Armut", "Çilek", "Karpuz"]
print(f"shuffle öncesi liste: {liste}")
random.shuffle(liste)
print(f"shuffle sonrası liste: {liste}")
print(f"Rastgele eleman: {random.choice(liste)}")
print(f"Rastgele k tane benzersiz eleman: {random.sample(liste, 2)}")

print(f"Normal dağılım kümesi içinden: {random.gauss(50, 20)}")
# Sınav ort: 50, std: 20 olsun. Notumuz kaç gelmiş olabilir?

# Pratik - Monte Carlo pi sayısı tahmini
# 1 br'lik kareye atılan okların çeyrek daireye düşme olasılığı pi / 4
def pi_tahmin_et(deneme_sayisi):
    daire_ici = 0
    for deneme in range(deneme_sayisi):
        x = random.random()
        y = random.random()
        if x**2 + y**2 <= 1:
            daire_ici += 1
    return 4 * daire_ici / deneme_sayisi

print("10 dememe:", pi_tahmin_et(10))
print("1000 deneme:", pi_tahmin_et(1000))
print("100000 deneme:", pi_tahmin_et(100000))