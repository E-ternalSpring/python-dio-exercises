texto = input("Informe um texto: ")
VOGAIS = "AEIOU" #Declarando constante

#Estrutura de repetição utiliando um iterável
for letra in texto: #Para cada letra (item) dentro da variável texto
    if letra.upper() in VOGAIS: #Se a letra, transformada em maiúscula, estiver contida na constante VOGAIS
        print(letra, end=" ") #Exiba na tela, "end=" mantém caracteres na mesma linha
else:
    print() #Adiciona uma quebra de linha
    print("Executa no final do laço")

#Construindo uma tabuada de 5 com a estrutura de repetição for e a função built-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")
