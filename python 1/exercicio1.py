#faça um programa que mostre os numeros de 5 até 50 na tela 

for i in range (5,51):
    print(i)







# faça um programa que mostre os numeros de 10 a 100, porém apenas os que forem divisiveis por 3 e 5 ao mesmo tempo 


for i in range(10,101):
    if i % 3 == 0 and i % 5 ==0:
        print(i)