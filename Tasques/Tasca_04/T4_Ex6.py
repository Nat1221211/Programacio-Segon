# Arxiu: T4_Ex6.py
# Autor: Bernat Puig Casals
# Data: 26 de Novembre de 2025
# Descripcio:
# Creem una funció que donada una llista diu quins numeros coincideixen en la seva posicio.

import os
import random

def LlistaNumerica():
    llista = []
    try:
        print("Digues una cadena de numeros seprats per comes... (1,2,7,9,10...)")
        nums = input("Digues una cadena de numeros: ")
        numllista = list(nums)
        num = ""
        for j in range(len(numllista)-1,-1,-1):
            if numllista[j] == ",":
                llista.append(num)
                num = ""
            else:
                if num == "":
                    num = numllista[j]
                else:
                    num = numllista[j] + num
        llista.append(num)
        llista.sort(reverse=True)
        llista = list(map(lambda x: int(x), llista))
        print(f"La llista té: {len(llista)} elements.")
        print(f"La mitjana és: {round(sum(llista) / len(llista), 2)}.")
        parells = 0
        imparells = 0
        for p in llista:
            if p % 2 == 0:
                parells += 1
            else:
                imparells += 1
        print(f"Té {parells} parells, i {imparells} imparells.")
    except ValueError:
        print("Ha d'introduir un numero, no un caracter diferent...")

def main():
    print("!! - Llista Numerica - !!")
    LlistaNumerica()
        
    
    

if __name__ == "__main__":
    main()