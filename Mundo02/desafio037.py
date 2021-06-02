num = int(input('Insira o número que deseja converter: '))
print('1 binário\n2 octal\n3 hexadecimal')
conv = int(input('Para qual linguagem você deseja converter?'))
if conv == 1:
    print(f'O valor binário do número {num} é: {bin(num)}')
elif conv == 2:
    print(f'O valor octal do número {num} é: {oct(num)}')
elif conv == 3:
    print(f'O valor hexadecimal do número {num} é {hex(num)}')
else:
    print('Número inválido! Insira um dos números apresentados acima.')
