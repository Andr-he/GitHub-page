Numeros = [float (input())for i in range(6)]

Positivo = len([i for i in Numeros if i > 0])
print(f'{Positivo} Valores positivos')
Negativo = len([i for i in Numeros if i < 0])
print(f'{Negativo} Valores negativos')
