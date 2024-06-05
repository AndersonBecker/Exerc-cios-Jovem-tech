#Escreva um programa que receba o nome, idade, e bairro e mostre na tela.
nome = str(input("Digite seu nome: "))
idade = int(input("Digite a idade: "))
bairro = str(input("Digite o bairro:"))
print(nome, idade, bairro)

#Usando as mesma variáveis contrua uma frase de apresentação incrementando uma profissão.
nome = str(input("Informe seu nome:"))
idade = int(input("Informe sua idade:"))
profissão = input("Informe sua profissão:")
bairro = input("Informe seu bairro:")

#Escreva um programa que diga sua idade:
ano_nascimento = int(input("Informe sua data de nascimento:"))
ANO = 2024
nome = input("Agora informe seu nome:")

print("Olá",nome," consigo ver aqui que você tem",(ANO - ano_nascimento), "seja bem vindo ao JovemTech")

#Faça um programa que mostre a tabuada do número digitado.,
numero = int(input("Digite um número para ver sua tabuada: "))
print("{} * {} = {}".format(numero, 1, numero*1))
print("{} * {} = {}".format(numero, 2, numero*2))
print("{} * {} = {}".format(numero, 3, numero*3))
print("{} * {} = {}".format(numero, 4, numero*4))
print("{} * {} = {}".format(numero, 5, numero*5))
print("{} * {} = {}".format(numero, 6, numero*6))
print("{} * {} = {}".format(numero, 7, numero*7))
print("{} * {} = {}".format(numero, 8, numero*8))
print("{} * {} = {}".format(numero, 9, numero*9))
print("{} * {} = {}".format(numero, 10, numero*10))