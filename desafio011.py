altura = float (input ('Insira a altura da parede: '))
largura = float (input ('Insira a largura da parede: '))
parede = altura*largura
tinta = parede/2
print (f'A área da parede é de {parede}m², logo, necessita de {tinta} litros de tinta.')


print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(altura, largura, parede))
print('Para pintar essa parede são necessário {} l de tinta'.format (tinta))