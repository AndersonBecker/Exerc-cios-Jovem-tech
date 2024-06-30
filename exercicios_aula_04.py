# EXERCÍCIOS FINAIS

# 1 - Escreva um programa que receba dois números e imprima o maior deles.
numero_1 = int(input('Valor 1: '))
numero_2 = int(input('Valor 2: '))

if numero_1 > numero_2:
    print('Primeiro valor é maior', numero_1)
else:
    print('Segundo valor é maior ', numero_2)

# 2 -Elabore um programa que imprima se dois números digitados são iguais, senão, imprima que são diferentes
#  e quais são os números.
numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

if numero_1 == numero_2:
    print('Os dois números digitados são iguais!')
else:
    print('Os números são diferentes!')

# 3 - Faça um programa que some suas notas e calcule a média final, dizendo se está aprovado ou reprovado.
a_1 = float(input('Informe nota da A1: '))
a_2 = float(input('Informe nota da A2: '))
a_3 = float(input('Informe nota da A3: '))
MEDIA = (a_1 + a_2 + a_3) / 3

if MEDIA >= 8:
    print('Você está aprovado!')
    print('Sua média foi de:',MEDIA)
elif MEDIA < 8:
    print('Você está reprovado!')
    print('Sua média foi de:', MEDIA)

# 4 - Faça um programa que leia a altura e peso de uma pessoa, calcule o peso ideal, índice de IMC, utilizando a seguinte fórmula:
# IMC = peso / (altura ** 2)
altura = float(input('Informe sua altura: '))
peso = float(input('Informe seu peso: '))
IMC = peso / (altura ** 2)

if IMC >=0 or IMC < 18.5:
    print('Você é considerado com nível de magreza')
elif IMC > 18.5 or IMC < 25:
    print('Você é considerado com peso Normal')
elif IMC >= 25 or IMC <= 30:
    print('Você é considerado com sobrepeso.')
elif IMC > 30:
    print('Você é considerado obeso.')
else:
    print('Valor inválido.')

# 5 - Crie um menu funcional de um caixa eletrônico onde mostre para o usuário o valor em conta, saque, depósito e sair.
saldo_total = 0

print('SEJA BEM VINDO AO SEU CAIXA ELETRÔNICO')

while True:
    print('''Informe qual operação deseja:
    [1] Ver Saldo
    [2] Depositar
    [3] Sacar
    [4] Sair''')

    menu = input('Opção: ')
    
    if menu == '1':
        print(f'Seu saldo atual é de {saldo_total:.2f} reais.')
    elif menu == '2':
        print('Depósito')
        depositar = float(input('Qual valor deseja depositar: '))
        saldo_total = depositar + saldo_total
        print('Depósito realizado com sucesso.\n')
    elif menu == '3':
        print('Saque')
        sacar = float(input('Qual valor a ser sacado: '))
        if saldo_total > sacar:
            saldo_total = saldo_total - sacar
            print('Saque realizado\n')
        else:
            print('Saldo indisponível.\n')
    elif menu == '4':
        print('Obrigado por utilizar nossos serviços')
        break
    else:
        print('Opção inválida')

# 6 - 