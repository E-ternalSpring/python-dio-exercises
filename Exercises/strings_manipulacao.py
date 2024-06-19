curso = "pYthOn"

print(curso.upper()) #Converte todos os caracteres para maiúsculas

print(curso.lower()) #Converte todos os caracteres para minúsculas

print(curso.title()) #Converte os primeiros caracteres das palavras para maiúsculas, e o restante para minúsculas

#Eliminando espaços em branco
curso2 = "    Python  "

print(curso2.strip() + ".") # + "." para melhorar a visualização do resultado

print(curso2.lstrip() + ".") #Remove espaços a esquerda (left)

print(curso2.rstrip() + ".") #Remove espaços a direita (right)

#Junções e centralização
curso3 = "Python"

print(curso3.center(10, "#")) #Centraliza a string e mantém o número de caracteres desejado
#>>> "##Python##"

print("-".join(curso3)) #Insere um caractere após cada caractere da string
#>>> "P-y-t-h-o-n"
