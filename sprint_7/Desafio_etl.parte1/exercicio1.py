import configparser
import boto3
from datetime import datetime

# Cria objeto ConfigParser e lê as credenciais
config = configparser.ConfigParser()
config.read('./credentials.ini')

# Recupera as chaves e o token
AWS_ACCESS_KEY_ID = config.get('DEFAULT', 'aws_access_key_id')
AWS_SECRET_ACCESS_KEY = config.get('DEFAULT', 'aws_secret_access_key')
AWS_SESSION_TOKEN = config.get('DEFAULT', 'aws_session_token')

BUCKET_NAME = 'bucketdesafio'


aws_session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    aws_session_token=AWS_SESSION_TOKEN,
    region_name='us-east-1'
)
s3 = aws_session.client('s3')



# Lista dos buckets
buckets = [b['Name'] for b in s3.list_buckets()['Buckets']]

if BUCKET_NAME not in buckets:
    s3.create_bucket(Bucket=BUCKET_NAME)
    print(f'Bucket {BUCKET_NAME} foi criado')
else:
    print(f'O Buket {BUCKET_NAME} já existe')

year = datetime.now().year
month = datetime.now().month
day = datetime.now().day

with open('./files_csv/movies.csv', 'rb') as movies, open('./files_csv/series.csv', 'rb') as series:
    s3.upload_fileobj(movies, BUCKET_NAME, f'Raw/Local/CSV/Movies/{year}/{month}/{day}/movies.csv')
    s3.upload_fileobj(series, BUCKET_NAME, f'Raw/Local/CSV/Series/{year}/{month}/{day}/series.csv')