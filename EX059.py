from time import sleep

print('=-='*15)
n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
opr = 0

while opr != 5:
    print("""Escolha uma das opções a baixo:
[1] Soma
[2] Multiplicação
[3] Maior
[4] Novos Numeros
[5] Sair do programa""")
    opr = int(input('Por Favor escolha uma operação: '))

    if opr == 1:
        s = n1+n2
        print(f'O Resultado da sua Soma é de {s}')
    elif opr == 2:
        multi = n1*n2
        print(f'O Resultado da sua Multiplicação é de {multi}')
    elif opr == 3:
        if n1 > n2:
            print(f'O Maior entre {n1} e {n2} é {n1}')
        else:
            print(f'O Maior entre {n1} e {n2} é {n2}')
    elif opr == 4:
        n1 = int(input('Por favor digite o primeiro numero: '))
        n2 = int(input('Por favor digite o segundo numero: '))
    elif opr > 5:
        print('Opção invalida tente novamente!')
    else:
        print('Finalizando ...')
    print('=-='*15)
    sleep(2)
print('Volte sempre <3')
print('=-='*15)