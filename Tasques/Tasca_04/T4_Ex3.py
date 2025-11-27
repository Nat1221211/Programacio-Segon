# Arxiu: T4_Ex3.py
# Autor: Bernat Puig Casals
# Data: 25 de Novembre de 2025
# Descripcio:
# Creem una funció que demana un numero i un nom, diu el nom la quantitat de vegades del numero.

import os

def Mostrar():
    num = 0
    try:
        num = int(input("Digues un numero: "))
        if num == 0:
            print("Error !!")
        else:
            try:
                nom = input("Digues el teu nom: ")
            except ValueError:
                print("Has de dir un Nom")
    except ValueError:
        print("Ha d'introduir un numero...")
    if num < 0:
        num = abs(num)
        print("El numero hauria de ser positiu...")
    for i in range(num):
        if i != num -1:
            print(nom, end=", ")
        else:
            print(nom, end=".")

def main():
    print("!! - Mostrar Nom - !!")
    Mostrar()

    

if __name__ == "__main__":
    main()