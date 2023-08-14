import json
import requests
import boto3
from datetime import datetime

def get_movies_by_genre(api_key, genre_id, limit=20):
    movies = []
    page = 1

    while len(movies) < limit:
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre_id}&page={page}"
        try:
            response = requests.get(url)
            response.raise_for_status()  # Vai levantar uma exceção se a resposta não for 200 OK
            results = response.json().get('results', [])
        except requests.RequestException as e:
            print(f"Erro ao chamar API para o gênero {genre_id} na página {page}: {e}")
            results = []
        
        if not results:
            break
        
        movies.extend(results)
        page += 1

    return movies[:limit]  # garantindo que só retornamos 20 filmes

def lambda_handler(event, context):
    print("Iniciando a função lambda_handler...")

    # Autenticação na API TMDb
    api_key = "b5d1d"
    
    # Lista de gêneros a serem buscados
    genre_ids = {
        "Ação": 28,
        "Comédia": 35,
        "Ficção Científica": 878,
        "Romance": 10749,
        "Drama": 18
    }
    
    all_movies = []
    
    # Iterando por cada gênero para coletar os filmes
    for genre_name, genre_id in genre_ids.items():
        movies = get_movies_by_genre(api_key, genre_id)
        
        # Imprimir a quantidade de filmes coletados para esse gênero
        print(f"{genre_name}: {len(movies)} filmes coletados.")
        
        all_movies.extend(movies)
    
    # Aqui, vamos imprimir a quantidade de filmes coletados para diagnóstico
    print(f"Total de filmes coletados: {len(all_movies)}")

    # Configuração do S3
    s3 = boto3.client('s3')
    bucket = 'bucketdesafio2'

    # Formatar a data atual no formato ano/mês/dia
    now = datetime.now()
    date_path = now.strftime('%Y/%m/%d')

    # Criar o caminho do arquivo seguindo o padrão especificado
    object_key = f'Raw/TMDB/JSON/{date_path}/tmdb_data.json'

    try:
        # Fazer upload dos dados para a zona RAW do S3
        s3.put_object(Bucket=bucket, Key=object_key, Body=json.dumps(all_movies))
    except Exception as e:
        print(f"Erro ao salvar os dados no S3: {e}")
        return {
            'statusCode': 500,
            'body': json.dumps('Erro ao salvar os dados no S3!')
        }

    print("Função lambda_handler concluída com sucesso.")
    return {
        'statusCode': 200,
        'body': json.dumps('Dados do TMDb coletados com sucesso e armazenados no S3!')
    }