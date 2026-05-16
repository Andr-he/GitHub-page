DiaA = int(input().split()[1])
HoraA, MinutoA, SegundoA = map(int, input().split(' : '))
DiaB = int(input().split()[1])
HoraB, MinutoB, SegundoB = map(int, input().split(' : '))

segundos = (SegundoB - SegundoA)%60
Segundomaior = SegundoA > SegundoB
Minuto = (MinutoB - MinutoA - int(Segundomaior))%60
MinutoMaior = MinutoA > MinutoB 
Horas = (HoraB - HoraA - int(Segundomaior) or int(MinutoMaior))%24
Horamaior = HoraA > HoraB
Dias = (DiaB - DiaA - int(Segundomaior) or int(MinutoMaior) or int(Horamaior))



print(f'{Dias} dia(s)')
print(f'{Horas} hora(s)')
print(f'{Minuto} minuto(s)')
print(f'{segundos} segundo(s)')

