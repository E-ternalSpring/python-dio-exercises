def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234") # Passando valores de forma sequencial
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234") # Passando conjunto chave-valor
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"}) # Passando dicionário
