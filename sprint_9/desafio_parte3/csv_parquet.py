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

# Lendo os dados do CSV no bucket 'bucketdesafio'
datasource0 = glueContext.create_dynamic_frame.from_catalog(database="desafio3-parte1", table_name="24")

# Renomeando as colunas para CamelCase
renamed_data = datasource0.rename_field("tituloprincipal", "tituloPincipal") \
                           .rename_field("titulooriginal", "tituloOriginal") \
                           .rename_field("anolancamento", "anoLancamento") \
                           .rename_field("genero", "genero") \
                           .rename_field("notamedia", "notaMedia") \
                           .rename_field("numerovotos", "numeroVotos")

# Selecionando apenas as colunas desejadas
selected_cols = ["tituloPincipal", "tituloOriginal", "anoLancamento", "genero", "notaMedia", "numeroVotos"]
selected_data = SelectFields.apply(frame = renamed_data, paths = selected_cols)

# Salvando os dados em formato Parquet no bucket 'bucketdesafio3'
output_path = "s3://bucketdesafio3/TRT/Movies/movies.parquet"
selected_data.toDF().write.mode("overwrite").parquet(output_path)

# Commit do job
job.commit()


