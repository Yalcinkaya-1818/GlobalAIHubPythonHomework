import random
print('Adam Asmaca')
k=input('Kullanıcı adınızı giriniz.')   
print(f'Welcome {k}')
kelimeler=["TARÇIN","KARAMEL","BULUT"]
hak=3
bildi=False
kelime=kelimeler[random.randint(0,len(kelimeler)-1)]
tahmin_alani=[" "]*len(kelime)
print(tahmin_alani)
while True:
    if hak==0:
        print("Oyun bitti. Maalesef oyunu kaybettiniz.")
        break
    if not " " in tahmin_alani:
        print("Oyunu Bitti. Tebrikler kazandınız.")
        break
    sayac=0
    harf_al=input("Harf girin: ").upper()
    for i in range(len(kelime)):
        if harf_al==kelime[i]:
            tahmin_alani[sayac]=harf_al
            bildi=True
        sayac+=1
    if bildi==False:
        hak-=1
    bildi=False
    print("Durum: ",tahmin_alani)
    print("Hak: ",hak)
