opcao = -1

#Estrutura de repetição com loops indefinidos
while opcao != 0: #Enquanto a variavel for diferente de 0
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: ")) #3 opções serão exibidas na tela

    if opcao == 1: #1 segue o loop
        print("Sacando...")
    elif opcao == 2: #2 segue o loop
        print("Exibindo extrato...")
else: #0 termina o loop
    print("Obrigada por utilizar o nosso sistema bancário, até logo!")
