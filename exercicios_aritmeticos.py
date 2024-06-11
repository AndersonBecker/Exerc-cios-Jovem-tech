# multiplicação, divisão, exponenciação divisão inteira e resta 1
print(5 / 2)
print(5 // 2)
print(5 * 2)
print(5 ** 2)
print(10 % 3)

#Operadores de atribuição +=, -=, *=, /=, dentre outros.
valor = 100
valor += 100
print(valor)

#Usando operadores lógicos.
saldo = 1000
saque = 250
limite = 100
saldo >= saque and saque <= limite

# Operador de Identidade.
curso = "Jovem Tech"
nome_curso = curso
saldo, limite = 200, 200

print(curso is not nome_curso)

# Operador de associação.(não esquecer que o Python é case sensitive)
curso = "Projeto Jovem Tech"
materiais = ['lapis', 'borracha', 'caneta']

print('borracha' in materiais)
print('Jovem' in curso)
print('Tech' not in curso)
print(materiais[1])

# FOR percorre lista
lista = ['aviao', 'fone', 'carro', 'violao', 'prato', 'sofa']
for i in lista:
    print(sorted(i))

# ************** EXERCÍCIOS ****************
#1 - Use o input para informar dois valores e printe a subtração deles.
a = input("Informe valor para A: ")
b = input("Informe valor para B: ")
subtrai = int(a) - int(b)
print("A subtração dos valores é: ", subtrai)

#2 - Usando input leia 3 valores e mostre a resposta da multiplicação na tela.
valor_1 = input("valor 1: ")
valor_2 = input("valor 2: ")
valor_3 = input("valor 3: ")
multiplica = int(valor_1) * int(valor_2) * int(valor_3)
print("Valores multiplicados é: ", multiplica)

#3 - Faça um código usando float para mostrar a divisão de 2 números que mostre as casas decimais.
valor_1 = input("valor 1: ")
valor_2 = input("valor 2: ")
divide = float(valor_1) / float(valor_2)
resultado = round(divide, 2)
print("valor dividido é: ",resultado)

#4 - Usando módulo(%) informe dois valores, divida-os e mostre o resultado da sobra.
x = 10
y = 3
print(x % y)

#5 - Informe dois valores use exponenciação(**) e mostre na tela.
v1 = 3
v2 = 2
print(v1 ** v2)

