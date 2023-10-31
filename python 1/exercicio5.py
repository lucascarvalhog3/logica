#Escreva um programa que solicite ao usuario um numero inteiro e imprima a tabuada desse numero, de 1 a 10.

numero = int(input("Digite um número: "))

for i in range(1,11):
    print(f"{numero} x {i} = {numero * i}")