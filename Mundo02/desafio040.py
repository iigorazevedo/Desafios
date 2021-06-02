nota1 = int(input('Insira a primeira nota: '))
nota2 = int(input('Insira a segunda nota: '))
media = (nota1+nota2)/2
if media < 5:
    print('Reprovado. Estude mais.')
elif media <=6.9:
    print('Em recuperação.')
else:
    print('Aprovado! Parabéns!')
