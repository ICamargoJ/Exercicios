preço = float(input('Informe o preço do produto: '))
forma = int(input("""Informe qual a forma de pagamento:
à vista no dinheiro/cheque digite [1]
à vista no cartão digite [2]
em 2x no cartão digite [3]
3x ou mais no cartão digite [4] """))
if forma == 1:
    desc = (preço*10)/100
    final = preço - desc
    print('Seu produto saira com o valor de {:.2f}.'.format(final))
elif forma == 2:
    desc = (preço*5)/100
    final = preço - desc
    print('Seu produto sairá por {:.2f}.'.format(final))
elif forma == 3:
    final = preço/2
    print('Voce pagará duas parcelas de {:.2f} sem JUROS.'.format(final))
elif forma == 4:
    juros = (preço*20)/100
    final = (preço + juros)
    parc = int(input('Quantas parcelas ? '))
    totparc = final / parc
    print('sua compra sera parcelada em {}x de {:.2f} COM JUROS.'.format(parc, totparc))
    print('Seu produto tera 20 por cento de juros e saira por {:.2f}.'.format(final))
else:
    final = 0
    print('Opcão de pagamento invalida, tente novamente!')
print('Sua compra de {:.2f} saira por {:.2f} no fimal.'.format(preço, final))
