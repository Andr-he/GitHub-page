Dias = int(input())

Anos= Dias//365
Dias = Dias%365
Meses = Dias//30
Dias = Dias%30

print(f'{Anos} ano(s)')
print(f'{Meses} mes(es)')
print(f'{Dias} dia(s)')
