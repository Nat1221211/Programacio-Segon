# Arxiu: T4_Ex4.py
# Autor: Bernat Puig Casals
# Data: 25 de Novembre de 2025
# Descripcio:
# Creem una funció que donada una llista diu si aquesta es simetrica.

import os
import random

def Simetria(llista):
    llistaI = [llista[x] for x in range(len(llista) -1, -1, -1)]
    os.system("cls")
    simetric = True
    for i in range(len(llista) - 1):
        if llista[i] != llistaI[i]:
            simetric == False
    if simetric == True:
        print(f"La llista: {llista} és simetrica.")
    else:
        print(f"La llista: {llista} no és simetrica.")
    print("Llista Invertida: ",llistaI)

def main():
    print("!! - Ser Simetric - !!")
    llista = []
    try:
        num = 0
        nums = random.randint(2, 12)
        print(f"Has de dir {nums} numeros.")
        for i in range(nums):
            num = int(input("Digues un numero: "))
            llista.append(num)
        Simetria(llista)
    except ValueError:
        print("Ha d'introduir un numero, no un caracter diferent...")
    

if __name__ == "__main__":
    main()