nome = "Emmanuelle"
idade = 27
profissao = "Programadora"
linguagem = "Python"

#Old Style
print("Olá, me chamo %s. Eu tenho %d anos de idade, trabalho como %s e estou matriculado(a) no curso de %s." % (nome, idade, profissao, linguagem))

#Método Format
print("Olá, me chamo {}. Eu tenho {} anos de idade, trabalho como {} e estou matriculado(a) no curso de {}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {0}. Eu tenho {1} anos de idade, trabalho como {2} e estou matriculado(a) no curso de {3}.".format(nome, idade, profissao, linguagem))

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado(a) no curso de {linguagem}.".format(nome=nome, idade=idade, profissao=profissao, linguagem=linguagem))

pessoa = {"nome": "Emmanuelle", "idade": 27, "profissao": "Programadora", "linguagem": "Python"} #Definindo "pessoa"

print("Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado(a) no curso de {linguagem}.".format(**pessoa)) # **pessoa definido no dicionário

#Método f-string (recomendado)
print(f"Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho como {profissao} e estou matriculado(a) no curso de {linguagem}.")

PI = 3.14159

print(f"Valor de PI: {PI:.2f}") #Definindo o número de casas decimais desejado na exibição
#>>> Valor de PI: 3.14

print(f"Valor de PI: {PI:10.2f}") #Adicionando espaços em branco antes da variável na string
#>>> Valor de PI:           3.14
