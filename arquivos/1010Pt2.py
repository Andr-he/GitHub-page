Codigo1, NumeroPecas1, ValorPecas1 = map(float, input().split())
Codigo2, NumeroPecas2, ValorPecas2 = map(float, input().split())

Pago = ((NumeroPecas1 * ValorPecas1) + (NumeroPecas2 * ValorPecas2))

print(f'VALOR A PAGAR: R$ {Pago:.2f}')   