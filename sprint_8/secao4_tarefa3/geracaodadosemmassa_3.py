import random
import names
import time
import os

# Definindo a semente de aleatoriedade
random.seed(40)

qtd_nomes_unicos = 3000
qtd_nomes_aleatorios = 10000000

# Gerando os nomes únicos
unique_names = [names.get_full_name() for _ in range(qtd_nomes_unicos)]

# Gerando os nomes aleatórios
random_names = [random.choice(unique_names) for _ in range(qtd_nomes_aleatorios)]

# Salvando os nomes em um arquivo
with open('nomes_aleatorios.txt', 'w') as f:
    for name in random_names:
        f.write("%s\n" % name)
