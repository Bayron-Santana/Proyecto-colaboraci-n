from operaciones import suma, resta, multiplicacion, division
from cuento import imprimir_cuento
from utilidades import es_par, es_impar, promedio


print("===================================")
print("      MI PROYECTO EN .PY")
print("===================================")

nombre = input("Escribe tu nombre: ")

print("\nHola", nombre)
print("Vamos a probar los módulos del proyecto.")

print("\n--- CALCULADORA ---")

numero1 = 20
numero2 = 5

print("Número 1:", numero1)
print("Número 2:", numero2)

print("Suma:", suma(numero1, numero2))
print("Resta:", resta(numero1, numero2))
print("Multiplicación:", multiplicacion(numero1, numero2))
print("División:", division(numero1, numero2))

print("\n--- UTILIDADES ---")

numero = 7

print("El número", numero, "¿es par?", es_par(numero))
print("El número", numero, "¿es impar?", es_impar(numero))

notas = [8, 9, 10]
print("Promedio de las notas:", promedio(notas))

print("\n--- MI CUENTO ---")
imprimir_cuento()

print("\n===================================")
print("       FIN...")
print("===================================")