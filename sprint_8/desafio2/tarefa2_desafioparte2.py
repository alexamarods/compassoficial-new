import json
import requests
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # Autenticação na API TMDb
    api_key = "a6867533c6f2d2af89d2f6e43bbb5d1d"
    url = f"https://api.themoviedb.org/3/movie/550?api_key={api_key}"
    response = requests.get(url)
    data = response.json()

    # Configuração do S3
    s3 = boto3.client('s3')
    bucket = 'bucketdesafio2'  # substitua pelo nome do seu bucket

    # Formatar a data atual no formato ano/mês/dia
    now = datetime.now()
    date_path = now.strftime('%Y/%m/%d')

    # Criar o caminho do arquivo seguindo o padrão especificado
    object_key = f'Raw/TMDB/JSON/{date_path}/tmdb_data.json'

    # Fazer upload dos dados para a zona RAW do S3
    s3.put_object(Bucket=bucket, Key=object_key, Body=json.dumps(data))

    return {
        'statusCode': 200,
        'body': json.dumps('Dados do TMDb coletados com sucesso e armazenados no S3!')
    }
 