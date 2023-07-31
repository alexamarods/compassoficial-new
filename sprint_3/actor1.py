file_path = r"D:\Documentos\Compass tudo\exemplo_pb\sprint_3\actors.csv"

# Abrir o arquivo CSV
with open(file_path, 'r') as file:
    # Ler as linhas do arquivo
    lines = file.readlines()

# Processar os dados
header = lines[0].strip().split(',')  # Cabeçalho
data = []

# Percorrer as linhas de dados
for line in lines[1:]:
    # Verificar se a vírgula está antes do "Jr."
    if ', Jr.' in line:
        # Remover a vírgula antes do "Jr."
        line = line.replace(', Jr.', ' Jr.', 1)  # Substituir apenas a primeira ocorrência

    # Dividir a linha em colunas
    row = line.strip().split(',')
  
    # Adicionar a vírgula antes de "Jr." novamente
    if ' Jr.' in row[0]:
        row[0] = row[0].replace(' Jr.', ', Jr.', 1)

    # Adicionar a linha de dados à lista
    data.append(row)

# Encontrar o índice da coluna 'Number of Movies'
num_movies_index = None
for i, column in enumerate(header):
    if column.strip() == 'Number of Movies':
        num_movies_index = i
        break

# Verificar se a coluna 'Number of Movies' foi encontrada
if num_movies_index is not None:
    # Inicializar variáveis para o ator com o maior número de filmes
    max_movies = 0
    actor_with_max_movies = ''

    # Percorrer as linhas de dados
    for row in data:
        # Obter os valores relevantes da linha
        actor = row[0]
        num_movies = row[num_movies_index]

        # Verificar se o valor da coluna 'Number of Movies' é um número válido
        if num_movies.isdigit():
            num_movies = int(num_movies)
            
            # Verificar se o número de filmes é maior que o máximo atual
            if num_movies > max_movies:
                max_movies = num_movies
                actor_with_max_movies = actor

    # Imprimir o resultado
    print(f"O 'Actor' com o maior número de 'Number of Movies' é '{actor_with_max_movies}' com {max_movies} filmes.")
else:
    print("A coluna 'Number of Movies' não foi encontrada no arquivo CSV.")