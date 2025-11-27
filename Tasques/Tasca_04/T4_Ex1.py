# Arxiu: T4_Ex1.py
# Autor: Bernat Puig Casals
# Data: 25 de Novembre de 2025
# Descripcio:
# Creem una funció que permet classificar una nota en un dels 4 apartats (Suspes, Aprovat, Notable, Excellent) despres
# d'arrodonir-la a un unic decimal.

import os

def ClassificarNota(Nota):
    Nota = round(Nota, 1)
    if Nota >= 9:
        print(f"Un {Nota} és un Excel·lent !!")
    elif Nota < 9 and Nota >= 7:
        print(f"Un {Nota} és un Notable !")
    elif Nota < 7 and Nota >= 5:
        print(f"Un {Nota} és un Aprovat.")
    elif Nota < 5:
        print(f"Un {Nota} és un Suspes...")



def main():
    print("!! - Classificadora de Notes - !!")
    num = -1
    while num > 10 or num < 0:
        try:
            os.system("cls")
            print("!! - Classificadora de Notes - !!")
            num = float(input("Digues una nota del 0 al 10: "))
            ClassificarNota(num)
        except ValueError:
            print("Ha d'introduir un numero del 0 al 10, incloent decimals.")
    

if __name__ == "__main__":
    main()