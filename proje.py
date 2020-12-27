class oys:
            dersKayit={}
            dersSayisi=0
            dersOrtalama=0
            dersNotlari={}
            count=3
            def __init__(self,name="",surname=""):
                self.name=name;
                self.surname=surname

                
            def adDegistir(self,yeniAd,yenisoyad):
                self.count-=1
                self.name=yeniAd
                self.surname=yenisoyad

                
            def notHesap(self):
                for x,y in self.dersKayit.items():
                    if (y[0]*0.3+y[1]*0.5+y[2]*0.2)>=90:
                        self.dersNotlari[x]="AA ile Geçtin"
                    elif 70<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<90:
                        self.dersNotlari[x]="BB ile Geçtin"
                    elif 50<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<70:
                        self.dersNotlari[x]="CC ile Geçtin"
                    elif 30<=int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<50:
                        self.dersNotlari[x]="DD ile Geçtin"
                    elif int(y[0]*0.30+y[1]*0.5+y[2]*0.2)<30:
                        self.dersNotlari[x]="FF ile Kaldın"
                for x,y in self.dersNotlari.items():
                    print(f"Ders Adi:{x},Ders Notu:{y}")


                
            def dersEkle(self,dersAdi,midterm,final,project):
                self.dersSayisi+=1
                self.dersAdi=dersAdi
                self.midterm=midterm
                self.final=final
                self.project=project
                self.dersKayit[self.dersAdi]=[self.midterm,self.final,self.project]
                

            def dersKayitYazdir(self):            
                return self.dersKayit


            
            def dersKayiKeys(self):
                count=1
                for x in self.dersKayit.keys():
                    print(f"Ders {count}:{x}")
                    count+=1

        case={
        1:"1-Ad Değiştir",
        2:"2-Ders Kaydı",
        3:"3-Ders Notu Hesapla",
        4:"4-Dersleri Göster",
        "Default":"Yanlış Tuş Girişi"}
         
        print("Öğrenci Kaydınızı Yapın Lütfen")
        name=input("Lütfen Adınızı Giriniz:")
        surname=input("Lütfen soyadınızı giriniz:")
        nesne=oys(name,surname)
        print("Öğrenci Kaydınız Başarılı.")
        dur=True
        
        while dur:
            print(f"Merhaba {nesne.name} {nesne.surname}")
            for x in case.values():
                if x in "Yanlış Tuş Girişi":
                    pass
                else:
                    print(x)
            switch=int(input("please enter someone:"))
           
            if switch==1:
                if(nesne.count>0):
                    yeniad=input(f"{nesne.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Ad Giriniz:")
                    yeniSoyad=input(f"{nesne.count} defa adınızı ve soyadınızı değiştirebilirsiniz Yeni Soyad Giriniz:")
                    nesne.adDegistir(yeniad,yeniSoyad)
                    print(f"Adınız ve soyadınız {nesne.name} {nesne.surname} olarak değiştirildi")
                else:
                    print("Hakkınız bitti")
            elif switch==2:
                if(nesne.dersSayisi>5):
                    print("Daha Fazla Ders Giremezsiniz")
                else:
                    dersAdi=input("Ders Adını Giriniz:")
                    vize=int(input("Vize Notunu Girniz:"))
                    final=int(input("Final Notunu Girniz:"))
                    proje=int(input("Proje Notunu Giriniz:"))
                    nesne.dersEkle(dersAdi,vize,final,proje)
                    print("Ders Kaydınız Başarılı")
            elif switch==3:
                if(nesne.dersSayisi>2):
                      nesne.netHesap()
                else:
                    print(f"Ders sayınız en az 3 olmalı. sizin ders sayınız: {nesne.dersSayisi}")
            elif switch==4:
                if(nesne.dersSayisi>0):
                    nesne.dersKayiKeys()
                else:
                    print("Dersiniz Yok Lütfen ders ekleyin")
            else:
                case["Default"]
            kontrol=input("Devam Etmek İstiyor musunz E/H")
            if dur=="e" or dur=="E":
                dur=True
            else:
                dur=False
                print("Tekrar Bekleriz")
