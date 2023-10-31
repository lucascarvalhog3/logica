# faça um programa que pede para o usuario escrever o seu nome e mostre na tela quantas letras "a" existe no nome digitado

# o nome { tal } possui {tantas}letras "a"



nome = str(input("digite seu nome: "))
contador = 0
for letra in nome:
    if letra.lower() == "a":
        contador += 1
        print(f"O nome {nome} possui {contador} letras 'a'")

        

