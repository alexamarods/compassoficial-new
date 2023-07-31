# Lista de nomes de animais
animal_list = ['gato', 'cachorro', 'elefante', 'leão', 'tigre', 'urso', 'zebra', 'girafa', 'hipopótamo', 'canguru', 
               'raposa', 'lobo', 'tubarão', 'panda', 'gorila', 'camelo', 'coelho', 'ornitorrinco', 'castor', 'falcão']

# Ordenar a lista
animal_list.sort()

# Imprimir os animais
for animal in animal_list:
    print(animal)

# Salvar a lista em um arquivo CSV
with open('animals.csv', 'w') as f:
    for animal in animal_list:
        f.write("%s\n" % animal)
