valor_prod = float(input('Insira o valor do produto: '))
valor_dinheiro = valor_prod-(valor_prod*0.1)
valor_cartao = valor_prod-(valor_prod*0.05)
valor_parc = valor_prod
valor_3x = valor_prod+(valor_prod*0.2)
forma = int(input('''Formas de pagamento:\n1 - Dinheiro ou Cheque \n2- À vista no cartão
3- 2x no cartão \n4- 3x ou mais vezes\nQual a forma de pagamento?'''))
if forma == 1:
    print(f'O valor a pagar em dinheir/cheque será de R$ {valor_dinheiro:.2f}')
elif forma == 2:
    print(f'O valor a pagar à vista no cartão é de R$ {valor_cartao:.2f}')
elif forma == 3:
    print(f'O valor a pagar em 2x no cartão é de R$ {valor_parc:.2f}')
elif forma >=4:
    print(f'O valor a pagar do produto parcelado é de R$ {valor_3x:.2f}')
