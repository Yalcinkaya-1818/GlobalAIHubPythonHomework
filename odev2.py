mylist=[]
mylist.append(input('İsminizi giriniz.'))
mylist.append(input('Soyadınızı giriniz.'))
mylist.append(int(input('Yaşınızı giriniz.')))
mylist.append(int(input('Doğum tarihini giriniz.')))
for i in range (0,4):
    print(mylist[i])
    if(i==3):
        if (mylist[2]<18):
            print('You can"'"t go out because it"'"s too dangerous.')
        else:
            print('You can go out to the screen.')

    
