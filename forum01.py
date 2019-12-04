# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 11:55:17 2019

@author: Gerson
"""

# Bibliotecas
import matplotlib.pyplot as plt
import math

# -- Programa principal --
# inicialização de variável
soma = 0

# entrada de dados
xi = float(input('Digite o valor inicial do intervalo: '))

xf = float(input('Digite o valor final do intervalo: '))
while xf<=xi:
    print('Erro! \\nO valor final deve ser maior do que o valor inicial!!')
    xi = float(input('Digite o valor inicial do intervalo: '))
    xf = float(input('Digite o valor final do intervalo: '))

base = 0.1

# plotagem do objeto
x = xi 
y2 = 0
while(x<=xf):

    if -10< x < 12.2:
        y = -4*x**2+4
    elif 12.3 < x < 22.3:
        y = -2*x**2+4

    plt.plot(x,y,marker='o',color='black')
    plt.bar(x,y,base)

#    plt.plot(x,y2,marker='o',color='black')
    
    soma = soma + (base*y)
    x = x + base

# exibição da área aproximada
print('\n\n*******************************')
print('Área aproximada:',soma,'u.a.')
print('*******************************')
# exibicao do grafico
plt.xlabel('x (m)')
plt.ylabel('y (m)')
plt.show()