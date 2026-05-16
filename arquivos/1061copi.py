MesA = int(input().split()[1])
DiaA, HoraA, MinutoA, SegundoA = map(int, input().split(' : '))
MesB = int(input().split()[1])
DiaB, HoraB, MinutoB, SegundoB = map(int, input().split(' : '))

segundos = (SegundoB - SegundoA)%60
Segundomaior = SegundoA > SegundoB
Minuto = (MinutoB - MinutoA - int(Segundomaior))%60
MinutoMaior = MinutoA > MinutoB 
Horas = (HoraB - HoraA - int(Segundomaior) or int(MinutoMaior))%24
Horamaior = HoraA > HoraB
Dias = (DiaB - DiaA - int(Segundomaior) or int(MinutoMaior) or int(Horamaior))%30
DiaMaior = DiaA > DiaB
Mes = (MesB - MesA - int(Segundomaior) or int(MinutoMaior) or int(Horamaior) or int(DiaMaior))
#Nao deu certo 

print(f'{Mes} mes(es)')
print(f'{Dias} dia(s)')
print(f'{Horas} hora(s)')
print(f'{Minuto} minuto(s)')
print(f'{segundos} segundo(s)')