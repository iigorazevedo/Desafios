from time import sleep
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
print('-'*40)
print('Analisando...')
sleep(3)
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
print('\n\n\n\n\n\n\nFIM DO PRIMEIRO MUNDO! VIVA!!!!!!')