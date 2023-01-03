from random import shuffle , randint
from string import ascii_letters , digits , punctuation

list = []
def password():
    xariflar_soni = int(input(" Parolingiz nechta xarifdan iborat bolsin : "))
    belgilar_soni = int(input(" Parolingiz nechta belgidan iborat bolsin : "))
    raqamlar_soni = int(input(" Parolingiz nechta raqamdan iborat bolsin : "))

    for xariflar_soni in range(0, xariflar_soni):
        x = randint( 0 , 53)
        tanlab_olingan_xarif = ascii_letters[x]
        list.append(tanlab_olingan_xarif)

    for belgilar_soni in range(0, belgilar_soni):
        b = randint(0, 33)
        tanlab_olingan_belgi = punctuation[b]
        list.append(tanlab_olingan_belgi)

    for raqamlar_soni in range(0, raqamlar_soni):
        tanlab_olingan_raqam = randint(0 ,10)
        list.append(tanlab_olingan_raqam)

    shuffle(list)

    parol = ""
    for  p in list:
        parol = parol + str(p)

    print(f"Sizning parolingiz quidagicha : {parol} ")


while True:
    print(password())
    povtor = input('''
        Yana urinib korishni uchun 'Y' bosing 
        Toxtatish uchun 'N' bosin : ''')
        
    if povtor.lower() == "y" :
        continue
    else:
        print("Kep turing !")
        break

