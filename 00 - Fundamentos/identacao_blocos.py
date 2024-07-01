def sacar(valor): #Definição da função, início do bloco da função após ":"
    saldo = 500 #Definição do saldo dentro da função sacar

    if saldo >= valor: #Início do bloco if dentro do bloco da função sacar
        print("Valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")
    #Fim do bloco if
    print("Obrigada por ser nosso cliente, tenha um bom dia!")
#Fim do bloco da função sacar
def depositar(valor): #Início do bloco da função depositar
    saldo = 500
    saldo += valor
#Fim do bloco
sacar (250)
