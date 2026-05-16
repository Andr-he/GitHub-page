Dias = int(input())

Anos= Dias//365
Dias = Dias%365
Meses = Dias//30
Dias = Dias%30

print(f'{Anos} anos(s),{Meses} mes(es),{Dias} dia(s).')

