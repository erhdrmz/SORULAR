toplam = 0
dizi = []
for i in range (1001) :
    yapılcak = i**i
    toplam += yapılcak
print (toplam%10000000000)
