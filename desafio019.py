import random
primeiro = input ('Digite o nome do primeiro aluno: ')
segundo = input ('Digite o nome do segundo aluno: ')
terceiro = input('Digite o nome do terceiro aluno:')
quarto = input ('Digite o nome do quarto aluno:')
lista = [primeiro, segundo, terceiro, quarto]
escolhido = random.choice(lista)
print ('O aluno escolhido foi {}'.format(escolhido))