cumle = input("cumle gırınız :")
print(cumle[::-1] )
print(cumle.split(' '))
harf=[]
sayi=[]
for i in(cumle):
    if not (i in harf):
        harf.append(i)
        sayi.append(1)
    else:
        sayi[harf.index(i)]=sayi[harf.index(i)]+1
print ("Harf --> Sayi")
for j in range(len(harf)):
    print (harf[j], " --> ", sayi[j])
tersi=cumle[::-1]
bolen=tersi.split(' ')
print (" Kelimeleri kendi içinde ters çeviren ",bolen[::-1])

unluharfler=["a","e","o","ö","u","ü","ı","i"]
unluharf=[]
unsuzharf=[]
for i in cumle:
    if i==unluharfler[0]or i==unluharfler[1]or i==unluharfler[2]or i==unluharfler[3]or i==unluharfler[4]or i==unluharfler[5]or i==unluharfler[6]or i==unluharfler[7]:
        unluharf.append(i)
    else:
        unsuzharf.append(i)
print("Ünlüler",unluharf)
print("Ünsüzler",unsuzharf)
if not unluharfler in unluharf:
                harf= harf.replace('i', 'ü')
                harf = harf.replace('ö')
print("unluharfler",unluharf)
