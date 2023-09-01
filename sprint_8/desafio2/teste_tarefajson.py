import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

# Argumentos iniciais
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicialização do Spark e Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Lendo os dados do JSON no bucket 'bucketdesafio2'
input_path = "s3://bucketdesafio2/Raw/TMDB/JSON/2023/08/12/"
datasource0 = glueContext.create_dynamic_frame.from_options("s3", {'paths': [input_path]}, format="json")

# Selecionando apenas as colunas desejadas 
selected_cols = ["title", "original_title", "release_date", "genre_ids", "vote_average", "vote_count"]
selected_data = SelectFields.apply(frame = datasource0, paths = selected_cols)

# Convertendo DynamicFrame para DataFrame para facilitar a manipulação
df = selected_data.toDF()

# Escrevendo os dados em arquivos JSON separados por gênero
for genre_id in df.select("genre_ids").distinct().rdd.flatMap(lambda x: x).collect():
    genre_df = df.filter(df.genre_ids.contains(genre_id))
    output_path = f"s3://bucketdesafio3/TRT/Movies/genre={genre_id}/"
    genre_df.write.mode("overwrite").json(output_path)

# Commit do job
job.commit()
