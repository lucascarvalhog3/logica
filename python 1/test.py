# faça um programa que pede para o usuário escrever 3 numeros inteiros e mostre na tela qual é o maior dos 3

n1 = float(input("digite um numero "))
n2 = float(input("digite um numero "))
n3 = float(input("digite um numero "))

if n1 >=n2 and n1 >=n3 :
    print (f' {n1} é o maior ')
elif n2 >=n1 and n2 >= n3 :
    print (f" {n2} é o maior ")
elif n3 >= n1 and n3 >= n2 :
    print(F' {n3} é o maior')

