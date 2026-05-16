Inicio, Fim = map(int, input().split())

if Inicio >= Fim:
    print(f'O JOGO DUROU {24 - Inicio + Fim} HORA(S)')
else:
    print(f'O JOGO DUROU {Fim - Inicio} HORA(S)')
    