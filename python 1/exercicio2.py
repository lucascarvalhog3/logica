# escreva um programa que solicite ao usuario um numero inteiro positivo e realize uma contagem regressiva a partir desse numero até zero,
# imprimindo cada numero no processo

numero = int(input("Digite um número: "))


while numero >=0:
    print(numero)
    numero -= 1
    
for i in range(numero, -1, -1):
    print(i)




