#funkcje

def test():

    baza   = ['pawel','anna']
    wyslij = input("wpisz imię ")

    for dane in baza:

        if  wyslij==dane:
            suma = dane
            return suma

        elif wyslij==None:
             return wynik

wynik = test()

if wynik==None:

   print("wystapil błąd")

else:

   print('Witaj' ,wynik)














































