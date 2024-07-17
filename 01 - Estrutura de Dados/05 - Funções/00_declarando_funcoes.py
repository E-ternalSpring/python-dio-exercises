def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome): # Será preciso declarar a variavel nome ao chamar a função
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"): # É opcional declarar a variavel nome ao chamar a função
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")
