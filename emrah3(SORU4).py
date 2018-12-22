sayi = False

toplam = 5

def makearray(sayi):
    array = []
    for iteration in range(int(10(sayi)+1)):

        array.append(sayi % 10)
        sayi //= 10

    return array

def checkarray(array1, array2):

        for digit in array1:
            if digit not in array2:
                return False
        return True

while sayi == False:
    for sayi1 in range(10 * toplam, (10 * (toplam + 1))//6):


        e=makearray(sayi1)
        m=makearray(sayi1*2)
        r=makearray(sayi1*3)
        a=makearray(sayi1*4)
        h=makearray(sayi1*5)
        d=makearray(sayi1*6)


        if checkarray(e,m) == checkarray(e,r) == checkarray(e,a) == checkarray(e,h) == checkarray(e,d) == True:
            print(sayi1)
            sayi = True

    toplam += 1
