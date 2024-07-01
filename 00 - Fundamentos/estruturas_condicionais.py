idade = int(input("Informe sua idade: ")) #Atribuí um valor inserido no teclado à var idade

MAIOR_IDADE = 18 #Constante
IDADE_ESPECIAL = 17

#Apenas com estrutura condicional "if"
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH! :D")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar a CNH, aguarde a maior idade ou idade especial para fazer as aulas teóricas. :(")

#Estrutura com "if" e "else"
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH! :D")
else:
    print("Ainda não pode tirar a CNH, aguarde a maior idade ou idade especial para fazer as aulas teóricas. :(")

#Estrutura com "if", "elif" e "else"
if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH! :D")
elif idade == IDADE_ESPECIAL:
    print("Ainda não pode tirar a CNH, mas já pode fazer as aulas teóricas. :)")
else:
    print("Ainda não pode tirar a CNH, aguarde a maior idade ou idade especial para fazer as aulas teóricas. :(")
