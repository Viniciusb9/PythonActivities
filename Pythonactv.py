## Lista de identificação do dia da semana por números ## 

num = int(input("numero de 1 a 7: "))

if num == 1:
    print('Segunda-feira')
elif num == 2:
    print('Terca-feira')
elif num == 3:
    print('Quarta')
elif num == 4:
    print('Quinta')
elif num == 5:
    print('Sexta')
elif num == 6:
    print('Sabado')
else:
    print('domingo')
    

## Calculo de media - aluno aprovado / reprovado ##

nota1 = float(input("Nota 1: "))
nota2 = float(input("nota 2: "))
nota3 = float(input("Nota 3: "))

nota3 = nota3 * 2

media = ((nota1 + nota2 + nota3)/4)

if media < 60:
    print('Aluno reprovado')
else:
    print('Aluno aprovado')
    


## Read the int number. If it's negative print invalid number; if positive calculate and print the log ## 

import numpy as np

num = int(input("Digite o numero: "))

if num < 0:
    print('numero inválido')
else:
    numf = np.log(num)
    print(numf)
    
    
    
## IMC calculator ##

def peso_ideal(altura, sexo):

    if sexo == 'f':

        print(f'Seu peso ideal é {62.1* altura - 44.7}kg')

    elif sexo == 'm':

        print(f'Seu peso ideal é {72.7* altura - 58}kg')

    else:
        print('Erro! O programa será fechado.')

altura = float(input('Digite sua altura: '))

sexo = str(input('Sexo [f/m]: '))

peso_ideal(altura, sexo)

## Read the int number. If it's positive, print the sqrt ^ 2, if not print invalid value ##

num = int(input('Insira um numero: '))

if num > 0:
    print(math.sqrt(num))
    print(num ** 2)
else:
    print('Valor invalido')
    
## 
