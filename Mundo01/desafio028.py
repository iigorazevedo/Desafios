from random import randint
from time import sleep
num_r = randint(1,5)
num = int(input('Digite o número que o COMPUTADOR pensou: '))
print('='*40)
sleep(4)
if num == num_r:
    print('Parabéns!! Você acertou!')
else:
    print(f'Infelizmente você errou! O número que o COMPUTADOR pensou foi {num_r}')