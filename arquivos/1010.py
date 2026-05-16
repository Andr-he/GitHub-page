
Codigo1 = int(input())
NumeroPecas1 = int(input())
ValorPeca1 = float(input())

Codigo2 = int(input())
NumeroPecas2 = int(input())
ValorPeca2 = float(input())

Pago = ((NumeroPecas1 * ValorPeca1) + (NumeroPecas2 * ValorPeca2))

print(f'VALOR A PAGAR: R$ {Pago:.2f}')
