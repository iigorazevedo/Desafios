from random import choice
jokenpo = ['Pedra','Papel','Tesoura']
maquina = choice(jokenpo)
print('Jo Ken Po Game!')
player = input('Escolha pedra, papel ou tesoura: ').capitalize()
if player == maquina:
    print(f' A máquina também escolheu {maquina}! O jogo empatou!')
elif maquina == 'Pedra' and player == 'Papel' or maquina == 'Papel' and player == 'Tesoura':
    print('Você ganhou!! {maquina} perde para {player}!!')
elif maquina == 'Pedra' and player == 'Tesoura' or maquina == 'Papel' and player == 'Pedra':
    print(f'O computador ganhou! {maquina} ganha de {player}')
