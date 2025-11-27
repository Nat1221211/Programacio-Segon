# Arxiu: T4_Ex2.py
# Autor: Bernat Puig Casals
# Data: 25 de Novembre de 2025
# Descripcio:
# Creem una funció que demana dos numeros i diu si son iguals o quin es més gran, si l'introduit no és un numero diu un error.

import os

def Comparar():
    num = 0
    try:
        valors = []
        for i in range(2):
            num = float(input("Digues un numero: "))
            valors.append(num)
        valors.sort(reverse=True)
        valors = list(map(lambda x: round(x, 3),valors))
    except ValueError:
        print("Ha d'introduir un numero...")
    if valors[0] != valors[1]:
        print(f"El numero {valors[0]} és major que el numeró {valors[1]}")
    else:
        print(f"El numero {valors[0]} és igual que el numeró {valors[1]}")

def main():
    print("!! - Comparar Numeros - !!")
    Comparar()
    

if __name__ == "__main__":
    main()