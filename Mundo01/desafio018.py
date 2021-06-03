import math
angulo = float(input('Insira o valor do ângulo'))
angulo_rad = math.radians(angulo)
seno = math.sin(angulo_rad)
cos = math.cos(angulo_rad)
tang = math.tan(angulo_rad)
print('O seno do ângulo informado é: {:.2f}\nO COSSENO é {:.2f}\nE a tangente é {:.2f}'.format (seno, cos, tang))