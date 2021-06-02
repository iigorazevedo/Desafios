from time import sleep
r1 = int(input('Digite o valor da primeira reta: '))
r2 = int(input('Digite o valor da segunda reta: '))
r3 = int(input('Digite o valor da terceira reta: '))
print('-'*40)
print('Analisando...')
sleep(1)
if r1 == r2 == r3:
    print('O triângulo é equilátero!')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print(' O triângulo é isósceles!')
else:
    print('o triângulo é escaleno.')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas acima podem formar um triângulo!')
else:
    print('As retas não podem formar um triângulo!')
