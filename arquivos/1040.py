N1,N2,N3,N4 = map(float, input().split())

Media = (N1*2 + N2*3 + N3*4 + N4*1)/10

if Media >= 7.0:
    print(f'Media: {Media:.2f}')
    print('Aluno aprovado.')
elif Media < 5.0:
    print(f'Media: {Media:.2f}')
    print('Aluno reprovado.')
elif 5.0 <= Media <= 6.9:
    print(f'Media: {Media:.2f}')
    print('Aluno em exame.')
    N5 = float(input())
    print(f' Nota do exame: {N5:.2f}')
    print(f'Media final: {(Media + N5)/2:.2f}')
    if (Media + N5)/2 >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')


