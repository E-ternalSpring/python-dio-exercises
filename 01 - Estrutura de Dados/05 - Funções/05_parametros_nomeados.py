# Antes da barra somento sequenciais, /, *, a partir do asterisco é obrigatório somente argumentos nomeados
def criar_carro(modelo, ano, placa, /, *, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
#criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", 1.0, "Gasolina")  # inválido
