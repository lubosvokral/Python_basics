import random

while True:
    mozne_volby = ["kámen", "nůžky", "papír"]
    volba_pocitac = random.choice(mozne_volby)
    volba_hrac = None

    while volba_hrac not in mozne_volby:
        volba_hrac = input("Vyber si kámen, nůžky nebo papír? ").lower()
    print(f"\nTvá volba je {volba_hrac}, volba počítače je {volba_pocitac}.\n")
    if volba_hrac == volba_pocitac:
        print(f"Oba hráči zvolili {volba_hrac}. Je to plichta")
    elif volba_hrac == "kámen":
        if volba_pocitac == "nůžky":
            print("Kámen rozbije nůžky, vyhráváš")
        else:
            print("Papír zabalí kámen, Prohráváš")
    elif volba_hrac == "nůžky":
        if volba_pocitac == "papír":
            print("Nůžky stříhají papír, Vyhráváš")
        else:
            print("Kámen rozbije nůžky, Prohráváš")

    elif volba_hrac == "papír":
        if volba_pocitac == "kámen":
            print("Papír zabalí kámen, vyhráváš")
        else:
            print("Nůžky stříhají papír, Prohráváš")
        

    
    hrat_znovu = input("Chcete si ještě zahrát? ").lower()
    if hrat_znovu.lower() != "ano":         
        break

print("Tak zase příště, Ahoj!")
