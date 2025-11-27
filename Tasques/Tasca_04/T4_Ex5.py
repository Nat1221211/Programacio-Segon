# Arxiu: T4_Ex5.py
# Autor: Bernat Puig Casals
# Data: 26 de Novembre de 2025
# Descripcio:
# Creem una funció que donada una llista diu quins numeros coincideixen en la seva posicio.

import os
import random

def Coincidents(llista):
    coincideix = []
    for i in range(len(llista)):
        if i == llista[i]:
            coincideix.append(i)
    if len(coincideix) == 0:
        print("En la llista no hi ha numeros coincidents amb la posició...")
    else:
        print(f"Les posicions {coincideix} coincideixen amb el seu valor !!")

def main():
    print("!! - Posicio Coinicident - !!")
    llista = []
    try:
        num = 0
        nums = random.randint(2, 12)
        print(f"Has de dir {nums} numeros.")
        for i in range(nums):
            num = int(input("Digues un numero: "))
            llista.append(num)
        Coincidents(llista)
    except ValueError:
        print("Ha d'introduir un numero, no un caracter diferent...")
    

if __name__ == "__main__":
    main()