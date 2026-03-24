num1 = eval(input("Escriu el primer valor: "))
num2 = eval(input("Escriu el segon valor: "))
lletra = input("Escriu una lletra: ")
if lletra == "a":
    suma = num1 + num2
    resultat = (suma//10)
    print(f'El resultat és {resultat}')
elif lletra == "b":
    mitjana = (num1 + num2)/2
    print(f'El resultat és {mitjana})