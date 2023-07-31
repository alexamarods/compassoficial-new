CREATE EXTERNAL TABLE IF NOT EXISTS meubanco.tabelanomes(
  nome string,
  sexo string,
  total int,
  ano int
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.lazy.LazySimpleSerDe'
WITH SERDEPROPERTIES (
 'serialization.format' = ',',
 'field.delim' = ','
)
LOCATION 's3://alexamarods.com/dados/'
