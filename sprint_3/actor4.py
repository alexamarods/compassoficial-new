file_path = r"D:\Documentos\Compass tudo\exemplo_pb\sprint_3\actors.csv"

frequencia_filmes = {}

with open(file_path, 'r') as file:
    lines = file.readlines()

header = lines[0].strip().split(',')

for line in lines[1:]:
    data = []
    field = ''
    
    for i, char in enumerate(line):
        if char == ',':
            if i + 1 < len(line) and line[i + 1] != ' ':
                data.append(field.strip())
                field = ''
            else:
                field += char
        else:
            field += char
    
    data.append(field.strip())
    
    filme = data[4]

    if filme in frequencia_filmes:
        frequencia_filmes[filme] += 1
    else:
        frequencia_filmes[filme] = 1

filmes_mais_frequentes = []
frequencia_maxima = 0

for filme, frequencia in frequencia_filmes.items():
    if frequencia > frequencia_maxima:
        filmes_mais_frequentes = [filme]
        frequencia_maxima = frequencia
    elif frequencia == frequencia_maxima:
        filmes_mais_frequentes.append(filme)

print("Filme(s) mais frequente(s):")
for filme in filmes_mais_frequentes:
    print(f" - {filme}")
print(f"Frequência: {frequencia_maxima}")