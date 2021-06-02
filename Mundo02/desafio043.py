peso = float(input('Qual o seu peso? '))
altura = float(input('Qual a sua altura? '))
imc = peso/(altura*altura)
if imc <18.5:
    print('Você está abaixo do peso ideal.')
elif imc <25:
    print('Você está no peso ideal!')
elif imc <30:
    print('Você está um pouco acima do peso.')
elif imc <=40:
    print('Você está com obesidade leve.')
else:
    print('Você está com obesidade mórbida.')
