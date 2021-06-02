from datetime import date
todays_date=date.today()
ano = int(input('Insira o ano do seu nascimento: '))
year = todays_date.year
soma = year - ano
if soma < 18:
    print('Ainda não chegou o seu período de alistamento! Apenas com 18 anos!')
elif soma == 18:
    print('Está na hora de se alistar e servir a pátria!')
else:
    print('Você tem mais de 18 anos! Já passou o tempo de alistamento, se você ainda não se alistou, procure uma unidade de alistamento imediatamente para regularizar a sua situação!')
