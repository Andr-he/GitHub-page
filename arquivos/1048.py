Salario = float(input())

percentual = 0
novoSalario = 0
reajuste = 0 

if Salario <= 400:
    percentual = 0.15
elif Salario <= 800:
    percentual = 0.12
elif Salario <= 1200:
    percentual = 0.10
elif Salario <= 2000:
    percentual = 0.07
else: 
    percentual = 0.04

novoSalario = Salario + Salario * percentual
reajuste = Salario * percentual

print(f'Novo salario: {novoSalario:.2f}')
print(f'Reajuste ganho: {reajuste:.2f}')
print(f'Em percentual: {(percentual * 100):.0f} %')