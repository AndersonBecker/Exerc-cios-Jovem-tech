# 1 - Crie um programa que uma conta tem 1000 reais depositado, onde o usuário informará o valor a ser sacado
# e o caixa eletrônico diga se o saldo é suficiente ou não suficiente.
saldo = 1000
saque = float(input('Qual valor será sacado:'))

if saldo >= saque:
    print('Saque realizado com sucesso')
else:
    print('Saldo insuficiente')


# 2 - Faça um programa que diga se você pode fazer ou não a CNH.
idade = int(input('Informe sua idade:'))

if idade >= 18:
    print('Você tem permissão pra começar as aulas')
else:
    print('Você ainda não completou 18 anos.')

# 3 - Escreva um programa onde o usuário informe sua idade e o programa diga se ele pode votar ou não,
# não esquecendo que existe uma excessão onde aos 16 anos o voto é facultativo.
idade = int(input('Digite sua idade:'))

if idade >= 18:
    print('Você é maior de idade, é obrigado a votar!')
elif idade >= 16:
    print('Você tem maioridade parcial, não é obrigado a votar!')
else:
    print('Você não tem idade suficiente para votar!')

# 4 - Crie um menu onde o usuário tenha a opção de sacar e imprimir extrato e sair do programa.
saldo = 1000
menu = int(input('''Escolha opção desejada
                 [1] Sacar
                 [2] Extrato
                 [3] Sair\n'''))

if menu == 1:
    valor = int(input('Digite valor desejado'))
    if valor > saldo:
        print('Saldo insuficiente')
    else:
        print('Saque realizado com sucesso')

elif menu == 2:
    print('Imprimindo seu extrato!')

elif menu == 3:
    exit('Encerrando o atendimento')
else:
    print('Comando inválido')

# Usando IF ternário
saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "falha"
print(f'{status} ao realizar o saque')