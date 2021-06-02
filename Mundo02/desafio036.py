valor = int(input('Qual o valor do imóvel? '))
salario = int(input('Qual o seu salário? '))
prazo = int(input('Em quantos anos serão pagas as prestações? '))
prazo = prazo*12
mensalidade = valor/prazo
if mensalidade < salario*0.3:
    print('Empréstimo aprovado!')
    print(f'O valor da mensalidade será de R$ {mensalidade:.2f}')
else:
    print('Empréstimo negado! Valor da parcela superior a 30%')
