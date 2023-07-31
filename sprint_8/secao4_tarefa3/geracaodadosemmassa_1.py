import random

# Gerar uma lista de 250 inteiros aleatórios entre 0 e 1000
num_list = [random.randint(0, 1000) for _ in range(250)]

# Reverter a lista
num_list.reverse()

# Imprimir a lista
print(num_list)
