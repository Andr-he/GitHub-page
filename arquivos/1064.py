Positivo = []
for i in range(6):
    Numero = float(input())
   
    if Numero > 0:
        Positivo.append(Numero)

print(f'{len(Positivo)} Valores positivos\n{(sum(Positivo)/len(Positivo)):.1f}')


