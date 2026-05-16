HoraInicial, MinutoInicial, HoraFinal, MinutoFinal = map(int, input().split())

if HoraInicial == HoraFinal:
    if MinutoInicial == MinutoFinal:
        print(f'O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
    elif MinutoInicial > MinutoFinal:
        print(f'O JOGO DUROU 23 HORA(S) E {60 - MinutoInicial + MinutoFinal} MINUTO(S)')
    elif MinutoInicial < MinutoFinal:
        print(f'O JOGO DUROU 0 HORA(S) E {MinutoFinal - MinutoInicial} MINUTO(S)')
elif HoraInicial > HoraFinal:
    if MinutoInicial == MinutoFinal:
        print(f'O JOGO DUROU {24 - (HoraInicial - HoraFinal)} HORA(S) E 0 MINUTO(S)')
    elif MinutoInicial > MinutoFinal:
        print(f'O JOGO DUROU {23-(HoraInicial - HoraFinal)} HORA(S) E {60-(MinutoInicial - MinutoFinal)} MINUTO(S)')
    elif MinutoInicial < MinutoFinal:
        print(f'O JOGO DUROU {24-(HoraInicial - HoraFinal)} HORA(S) E {MinutoFinal - MinutoInicial} MINUTO(S)')
elif HoraInicial < HoraFinal:
    if MinutoInicial == MinutoFinal:
        print(f'O JOGO DUROU {HoraFinal-HoraInicial} HORA(S) E 0 MINUTO(S)')
    elif MinutoInicial > MinutoFinal:
        print(f'O JOGO DUROU {HoraFinal-HoraInicial-1} HORA(S) E {60-(MinutoInicial-MinutoFinal)} MINUTO(S)')
    elif MinutoInicial < MinutoFinal:
        print(f'O JOGO DUROU {HoraFinal-HoraInicial} HORA(S) E {MinutoFinal-MinutoInicial} MINUTO(S)')
