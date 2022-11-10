from random import randrange
from symtable import Symbol

symbol_hrac = "x"
symbol_pocitac = "o"
def vyhodnot(pole):
    if "xxx" in pole:
        return("x")
    elif "ooo" in pole:
        return("o")
    elif "*" not in pole:
        return("!")
    else:
        return"*"

def tah(pole, pozice, symbol):
    return pole[:pozice] + symbol + pole[pozice+1:]

def tah_hrace(pole):
    while True:
        cislo_policka = int(input("Na které políčko chceš hrát? "))
        cislo_policka = cislo_policka - 1
        if cislo_policka > 0 and cislo_policka < 20 and pole[cislo_policka] == "*":
            return tah(pole, cislo_policka, symbol_hrac)
        else:
            print("Špatně zadaná pozice, zkus to znovu.")

def tah_pocitace(pole):
    while True:
        cislo_policka = randrange(len(pole))
        if pole [cislo_policka] == "*":
            return tah(pole, cislo_policka, symbol_pocitac)

def piskvorky1d():
    global symbol_hrac
    global symbol_pocitac
    symbol_hrac = input("Chceš hrát s kroužky nebo křížky, vyber 'x' nebo 'o' ? ")
    while symbol_hrac != "x" and symbol_hrac != "o":
        symbol_hrac = input("Špatně zadaný symbol, vyber si 'x' nebo 'o': ")

    if symbol_hrac == "x":
        symbol_pocitac = "o"
    elif symbol_hrac == "o":
        symbol_pocitac = "x"
    
    pole = 20 * "*"

    while True:       
        pole = tah_hrace(pole)
        print(pole)
        if vyhodnot(pole) != '*':
            break
        pole = tah_pocitace(pole)
        print(pole)
        if vyhodnot(pole) != '*':
            break
        
    if vyhodnot(pole) == '!':
        print('Remíza!')
    elif vyhodnot(pole) == symbol_hrac:
        print('Vyhrál jsi!')
    elif vyhodnot(pole) == symbol_pocitac:
        print('Vyhrál počítač!')

  

while True:
    piskvorky1d()
    hrat_znovu = input("Chcete si ještě zahrát? ").lower()
    if hrat_znovu.lower() != "ano":
        break
