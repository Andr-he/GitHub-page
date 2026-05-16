Nome = str(input())
SalarioFixo = float(input())
VendasEfetuadas = float(input())

Comissao = ((15 / 100) * VendasEfetuadas)
Total = (SalarioFixo + Comissao)

print(f'TOTAL = R$ {Total:.2f}')
