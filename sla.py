N1, N2 = map(float, input().split())

media = (N1 + N2) / 2

if media >= 7:
    print('Aprovado')
elif media >= 5 and media <= 6.9:
    print('Recuperação')
else:
    print('Reprovado')