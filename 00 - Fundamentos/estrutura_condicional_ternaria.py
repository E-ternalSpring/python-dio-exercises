saldo = 2000
saque = float(input("Insira o valor a ser sacado: "))

#Útil para verificações simples, compor mensagens. Promove a legibilidade e manutenção
status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
