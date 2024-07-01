lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

lista[0] = 5

print(lista)  # [5, "Python", [40, 30, 20]]
print(l2)  # [1, "Python", [40, 30, 20]]
