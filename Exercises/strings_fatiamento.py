nome = "Emmanuelle Espindola de Carvalho Pinto"

print(nome[0]) #Indíce zero
#>>> "E"

print(nome[:10]) #Índice de zero a 10 exclusivo
#>>> "Emmanuelle"

print(nome[11:]) #Índice de 11 inclusivo até o fim da string
#>>> "Espindola de Carvalho Pinto"

print(nome[11:20]) #Índice de 11 inclusivo até 20 exclusivo
#>>> "Espindola"

print(nome[11:20:2]) #Índice de 11 inclusivo até 20 exclusivo, passo 2
#>>> "Epnoa"

print(nome[:]) #Índice do começo ao fim
#>>> "Emmanuelle Espindola de Carvalho Pinto"

print(nome[::-1]) #Índice do começo ao fim, passo -1 (Inverte a string)
#>>> "otniP ohlavraC ed alodnipsE elleunammE"
