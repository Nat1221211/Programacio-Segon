# Arxiu: Index.py
# Autor: Bernat Puig Casals
# Data: 25 de Novembre de 2025
# Descripcio:
# Index per als exercics de la Tasca 4, aixi com un menu interactiu per a accedir a aquests.

import os
import T4_Ex1
import T4_Ex2
import T4_Ex3
import T4_Ex4
import T4_Ex5
import T4_Ex6

def main():
    print("!! - Index - !!")
    pos = 0
    while pos not in [1, 2, 3, 4, 5, 6, 7]:
        os.system("cls")
        print("!! - Index - !!")
        print("1 -> Classificació de Nota")
        print("2 -> Comparar Numeros")
        print("3 -> Mostrar Nom")
        print("4 -> Ser Simetric")
        print("5 -> Posicio Coincident")
        print("6 -> Llista Numerica")
        print("7 -> Sortir")
        try:
            pos = int(input("Digues el numero corresponent al exercici al que vols accedir: "))
        except ValueError:
            print("Has d'introduir un numero...")
    
        if pos == 1:
            T4_Ex1.main()
        elif pos == 2:
            T4_Ex2.main()
        elif pos == 3:
            T4_Ex3.main()
        elif pos == 4:
            T4_Ex4.main()
        elif pos == 5:
            T4_Ex5.main()
        elif pos == 6:
            T4_Ex6.main()
        elif pos == 7:
            print("Programa Finalitzat...")
        if pos != 7:
            input("\nPresiona per a continuar...")
            pos = 0

if __name__ == "__main__":
    main()