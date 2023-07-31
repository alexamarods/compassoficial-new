file_path = r"D:\Documentos\Compass tudo\exemplo_pb\sprint_3\actors.csv"
atores_faturamento = []

with open(file_path, 'r') as file:
    lines = file.readlines()

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

    ator = data[0]
    faturamento = float(data[1])  # Total Gross

    atores_faturamento.append((ator, faturamento))

atores_faturamento_ordenado = sorted(atores_faturamento, key=lambda x: x[1], reverse=True)

print("Lista de Atores por Faturamento Bruto Total:")
for ator, faturamento in atores_faturamento_ordenado:
    print(f"{ator}: {faturamento}")