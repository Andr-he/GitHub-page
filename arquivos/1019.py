N = int(input())


Dias = N//86400
N = N%86400
Horas = N//3600
N = N%3600
Minutos = N//60
N = N%60

print(f'{Dias}:{Horas}:{Minutos}:{N}')

