# Strings triplas ou multiplas linhas

nome = "Emmanuelle"

mensagem = f"""
Olá, meu nome é {nome},
    e eu estou aprendendo Python!
"""

# Strings múltiplas respeitam identação

print(mensagem)

#>>>
# 
# Olá, meu nome é Emmanuelle,
#   e eu estou aprendendo Python!
#

print(
    '''
    ========== MENU ==========
    
    1 - Depositar
    2 - Sacar
    3 - Sair
    
    ==========================
    
        Obrigada por usar nosso sistema!
    '''
    )
