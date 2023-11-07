# FAÇA UM PROGRAMA QUE PEDE PARA O USUÁRIO DIGITAR 5 FRUTAS
# E ADICIONA AS 5 FRUTAS NA LISTA DE FRUTAS
# ["UVA", "PÊRA", "MELÃO"]

lista_frutas = ["Uva", "Pêra", "Melão"]
qtde_frutas = int(input("Quantas frutas você quer adicionar? :"))

for i in range(qtde_frutas):
    fruta = str(input("Digite uma fruta: "))
    lista_frutas.append(fruta)

print(lista_frutas)