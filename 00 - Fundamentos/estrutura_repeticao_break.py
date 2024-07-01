while True:
    numero = int(input("Informe um número: "))

    if numero % 2 == 0:
        print("Par!") #Segue o loop para números par
    else:
        break #Quebra o loop caso o número seja ímpar

print("Ímpar!")

#Exibe apenas os números pares dentro de um range inserido
numero_maximo = int(input("Insira um número qualquer: "))

for numero in range(0, numero_maximo):
    
    if numero % 2 != 0:
        continue
    
    print(numero, end=" ")
