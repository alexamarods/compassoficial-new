import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Inicialização do Spark
sc = SparkContext()
spark = SparkSession(sc)

# Lendo os dados do JSON diretamente do S3
input_path = "s3://bucketdesafio2/Raw/TMDB/JSON/2023/08/12/tmdb_data.json"
df = spark.read.json(input_path)

# Selecionando apenas as colunas desejadas
selected_cols = ["title", "original_title", "release_date", "genre_ids", "vote_average", "vote_count"]
selected_data = df.select(*selected_cols)

# Salvando os dados em formato Parquet no S3
output_path = "s3://bucketdesafio3/TRT/Movies/2023/08/12/movies.parquet"
selected_data.write.mode("overwrite").parquet(output_path)
