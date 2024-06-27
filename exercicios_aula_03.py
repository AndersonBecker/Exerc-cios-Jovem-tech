#Primeiro modelo While
menu = -1

while menu !=0:
    menu = int(input(' [1] Sacar\n [2] Extrato \n [3] Sair \n'))

    if menu == 1:
        print('Saque realizado com sucesso')
    elif menu == 2:
        print('Imprimindo seu extrato.')
else:
    print('Obrigado por utilizar nossos serviços.')

# 1 - Faça uma lista com pelo menos 5 objetos e print na tela.
lista = ['carro', 'caminhão', 'moto', 'bicileta', 'avião']
for itens in lista:
    if itens in lista:
        print(itens, end=" - ")
print()

# 2 - Criar uma Range com step de 3 onde mostra na tela todos os números de 1 até 200.
for valor in range(0, 201, 3):
    print(valor,  end=' ')

# 3 - Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja
# inválido e continue pedindo até que o usuário informe um valor válido.
print('TENTE ADIVINHAR O NÚMERO')
NUMERO_CERTO = '7'
while True:
    numero = input('Chute um número: ')
    if numero == NUMERO_CERTO:
        print('Parabéns você acertou')
        break
    elif numero != NUMERO_CERTO:
        print('Não é este número que estou pensando')

# 4 - Faça um programa, utilizando while, que permita o usuário fazer contas de adição enquanto quiser.
print('Some Valores:')

while True:
    valor_1 = int(input('Digite primeiro número: '))
    valor_2 = int(input('Digite segundo número: '))
    
    soma = valor_1 + valor_2
    print('Valor da soma é', soma)

    menu = input('''Quer somar outro valor?
            [s] SIM
            [n] NÃO\n''')
    if menu == 's':
        print()
    elif menu == 'n':
        print('Obrigado por utilizar nossos serviços')
        break

# 5 - Faça um programa se o número digitado é par ou impar.
while True:
    numero = int(input('Digite um número: '))

    if numero == 20:
        break
    if numero % 2 == 0:
        print(f'Numero {numero} é par!')
        continue
    elif numero % 2 !=0:
        print(f'Número {numero} é impar!')
    
# 6 - Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando 
# uma mensagem de erro e voltando a pedir as informações.
login = input('Digite nome de usuário:')
senha = input('Digite sua senha: ')

while login == senha:
        print('Senha não pode ser igual login de usuário!')
        senha = input('senha: ')
print('Cadastro aprovado!!!') 

