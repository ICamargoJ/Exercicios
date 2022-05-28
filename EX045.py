from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesolra')
pc = randint(0,2)

print('-='*11)
print(""" Suas opções são:
[0] Pedra
[1] Papel
[2] Tesolra""")

print('-='*11)
jogador = int(input('Qual é a sua jogada ? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('O computador jogou: {}'.format(itens[pc]))
print('Voce jogou: {}'.format(itens[jogador]))

if pc == 0:
    if jogador == 0: #computador jogou PEDRA
        print('Voces EMPATARAM !!')
    elif jogador == 1:
        print('Voce VENCEU !!!!!')
    elif jogador == 2:
        print('Voce perdeu ;-;')
    else:
        print('JOGADA INVALIDA')

if pc == 1: #computador jogou PAPEL
    if jogador == 1:
        print('Voces EMPATARAM !!')
    elif jogador == 2:
        print('Voce VENCEU !!!!!')
    elif jogador == 0:
        print('Voce perdeu ;-;')
    else:
        print('JOGADA INVALIDA')
        
if pc == 2: #computador jogou TESOLTA
    if jogador == 2:
        print('Voces EMPATARAM !!')
    elif jogador == 0:
        print('Voce VENCEU !!!!!')
    elif jogador == 1:
        print('Voce perdeu ;-;')
else:
    print('JOGADA INVALIDA')
 