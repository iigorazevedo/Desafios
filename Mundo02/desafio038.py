num1 = int(input('Insira o primeiro número: '))
num2 = int(input('Insira o segundo número: '))
if num1 > num2:
    print(f'O número {num1} é maior que o {num2}')
elif num2 > num1:
    print(f'O número {num2} é maior que o {num1}')
elif num1 == num2:
    print('Os números são iguais!')
