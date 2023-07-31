from pyspark.sql import SparkSession
from pyspark.sql.functions import col, udf, when
from pyspark.sql.types import StringType, IntegerType
import random

spark = SparkSession \
                .builder \
                .appName("Exercicio Intro") \
                .getOrCreate()

# Lendo o arquivo
df_nomes = spark.read.text('/home/jovyan/work/nomes_aleatorios.txt').withColumnRenamed("value", "Nomes")


# Adicionando a coluna Escolaridade
escolaridade_list = ['Fundamental', 'Medio', 'Superior']
escolaridade_udf = udf(lambda _: random.choice(escolaridade_list), StringType())
df_nomes = df_nomes.withColumn("Escolaridade", escolaridade_udf(col("Nomes")))

# Adicionando a coluna Pais
paises_list = ['Argentina', 'Bolívia', 'Brasil', 'Chile', 'Colômbia', 'Equador', 'Guiana', 'Paraguai', 'Peru', 'Suriname', 'Uruguai', 'Venezuela', 'Guiana Francesa']
paises_udf = udf(lambda _: random.choice(paises_list), StringType())
df_nomes = df_nomes.withColumn("Pais", paises_udf(col("Nomes")))

# Adicionando a coluna AnoNascimento
ano_udf = udf(lambda _: random.randint(1945, 2010), IntegerType())
df_nomes = df_nomes.withColumn("AnoNascimento", ano_udf(col("Nomes")))

# Adicionando a coluna Geração
df_nomes = df_nomes.withColumn("Geração",
                               when(col("AnoNascimento").between(1944, 1964), "Baby Boomers")
                               .when(col("AnoNascimento").between(1965, 1979), "Geração X")
                               .when(col("AnoNascimento").between(1980, 1994), "Millennials")
                               .when(col("AnoNascimento").between(1995, 2015), "Geração Z")
                               .otherwise("Outros"))

# Selecionando as pessoas que nasceram neste século
df_select = df_nomes.filter(col("AnoNascimento") >= 2000)
df_select.show(10)

# Registrando a tabela temporária
df_nomes.createOrReplaceTempView ("pessoas")

# Executando o comando SQL
spark.sql("select * from pessoas where AnoNascimento >= 2000").show()

# Contando o número de pessoas que são da geração Millennials
millennials_count = df_nomes.filter(col("Geração") == "Millennials").count()
print(millennials_count)

# Contando o número de pessoas que são da geração Millennials com SQL
spark.sql("select count(*) from pessoas where `Geração` = 'Millennials'").show()


# Obtendo a quantidade de pessoas de cada país para cada geração
result = spark.sql("""
    select 
        Pais, 
        `Geração`,
        count(*) as Quantidade
    from pessoas
    group by Pais, `Geração`
    order by Pais, `Geração`, Quantidade
""")
result.show()