Valor = int(input()) 

Cedulas = [200, 100, 50, 20, 10, 5, 2, 1]

print(f'{Valor}')

for Nota in Cedulas:
    Quantidade = Valor//Nota
    Valor = Valor%Nota

    print(f'{Quantidade} nota(s) de R$ {Nota},00')
