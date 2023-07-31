WITH total_decada AS (
  SELECT 
    nome,
    (ano - MOD(ano, 10)) AS decada,
    SUM(total) as total_decada
  FROM 
    meubanco.tabelanomes
  WHERE 
    ano >= 1950 AND ano <= 2023
  GROUP BY 
    nome, (ano - MOD(ano, 10))
),
ranked AS (
  SELECT 
    nome,
    decada,
    total_decada,
    ROW_NUMBER() OVER(PARTITION BY decada ORDER BY total_decada DESC) as rank
  FROM 
    total_decada
)
SELECT 
  nome, 
  decada, 
  total_decada
FROM 
  ranked
WHERE 
  rank <= 3
ORDER BY 
  decada, 
  rank