conta_normal = True #Informa ao código que o tipo de conta é a normal
conta_universitaria = False

saldo = 2000
cheque_especial = 500
saque = int(input("Digite o valor do saque: "))

if conta_normal: #Estrutura condicional principal

    if saldo >= saque: #Estrutura condicional aninhada
        print("Saque realizado com sucesso!")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Saldo insuficiente.") #Tratativa caso nenhuma condição for atendida para a conta normal

elif conta_universitaria:

    if saldo >= saque: #Estrutura condicional aninhada
        print("Saque realizado com sucesso!")
    else:
        print("Saldo insuficiente.") #Tratativa caso nenhuma condição for atendida para a conta universitaria

else: #Tratativa caso nenhuma condição for atendida
    print("Sistema não reconhece a conta, por favor entre em contato com o seu gerente!")
