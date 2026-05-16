def Maior(A, B):
    return int((A + B+ abs (A- B))/2)

A, B, C = map(int, input().split())


print(f'{Maior(Maior(A, B), C)} eh o maior')