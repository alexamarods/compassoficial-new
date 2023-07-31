file_path = r"D:\Documentos\Compass tudo\exemplo_pb\sprint_3\actors.csv"
total_bruto = 0
quantidade_atores = 0

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

    actor = data[0]
    total_gross = float(data[1])  # Considerando que a coluna "Total Gross" está na posição 1

    total_bruto += total_gross
    quantidade_atores += 1

media_bruto_por_ator = total_bruto / quantidade_atores

print(f"A média de faturamento bruto por ator é: {media_bruto_por_ator}")

