import sys
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

# Argumentos iniciais
args = getResolvedOptions(sys.argv, ['JOB_NAME'])

# Inicialização do Spark e Glue Context
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Mapeamento dos genre_ids para seus respectivos nomes
genre_mapping = {
    16: "Animation",
    878: "Sci-Fi",
    27: "Horror",
    53: "Thriller",
    18: "Drama",
    12: "Adventure",
    10749: "Romance",
    28: "Action",
    10770: "TV Movie",
    9648: "Mystery",
    35: "Comedy",
    80: "Crime",
    10751: "Family",
    14: "Fantasy",
    10752: "War",
    36: "History"
}

# Função para converter lista de genre_ids em string de gêneros
def ids_to_genre_names(ids):
    return ','.join([genre_mapping.get(id, "Unknown") for id in ids])

convert_genre_udf = udf(ids_to_genre_names, StringType())

# Lendo e transformando o Parquet originado do JSON
json_path = "s3://bucketdesafio3/TRT/Movies/2023/08/12/movies.parquet/"
df_json = spark.read.parquet(json_path)
df_json_transformed = df_json.withColumn('genero', convert_genre_udf(df_json['genre_ids']))

# Renomeando colunas e removendo duplicatas
df_json_renamed = df_json_transformed.withColumnRenamed("original_title", "tituloOriginal") \
                                     .withColumnRenamed("release_date", "dataLancamento") \
                                     .withColumnRenamed("vote_average", "notaMedia") \
                                     .withColumnRenamed("vote_count", "numeroVotos")

df_json_deduplicated = df_json_renamed.dropDuplicates(['tituloOriginal', 'dataLancamento'])
df_json_final = df_json_deduplicated.drop('title', 'genre_ids')

# Lendo e renomeando o Parquet em português (originado do CSV)
csv_path = "s3://bucketdesafio3/TRT/Movies/movies.parquet/"
df_csv = spark.read.parquet(csv_path)
df_csv_renamed = df_csv.withColumnRenamed("titulooriginal", "tituloOriginal") \
                       .withColumnRenamed("anolancamento", "anoLancamento") \
                       .withColumnRenamed("notamedia", "notaMedia") \
                       .withColumnRenamed("numerovotos", "numeroVotos")

# Salvando os DataFrames refinados na camada Refined
refined_csv_path = "s3://bucketdesafio3/Refined/Movies/movies_from_csv.parquet"
refined_json_path = "s3://bucketdesafio3/Refined/Movies/movies_from_json.parquet"

df_csv_renamed.write.mode("overwrite").parquet(refined_csv_path)
df_json_final.write.mode("overwrite").parquet(refined_json_path)

# Commit do job
job.commit()

